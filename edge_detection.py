import numpy as np
from scipy.ndimage import gaussian_filter
import pygame

def detect_edges(surface, sigma=1.0, low_threshold=50, high_threshold=150):
    arr = np.mean(pygame.surfarray.array3d(surface), axis=2)
    arr = gaussian_filter(arr, sigma=sigma)
    
    Kx = np.array([[-1, 0, 1],
                  [-2, 0, 2],
                  [-1, 0, 1]])
    Ky = np.array([[1, 2, 1],
                  [0, 0, 0],
                  [-1, -2, -1]])
    
    Ix = np.zeros_like(arr)
    Iy = np.zeros_like(arr)
    rows, cols = arr.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            Ix[i, j] = np.sum(Kx * arr[i-1:i+2, j-1:j+2])
            Iy[i, j] = np.sum(Ky * arr[i-1:i+2, j-1:j+2])
    
    G = np.sqrt(Ix**2 + Iy**2)
    theta = np.arctan2(Iy, Ix)
    
    Z = np.zeros_like(G)
    angle = np.rad2deg(theta) % 180
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            try:
                q, r = 255, 255
                if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                    q = G[i, j+1]
                    r = G[i, j-1]
                elif 22.5 <= angle[i, j] < 67.5:
                    q = G[i+1, j-1]
                    r = G[i-1, j+1]
                elif 67.5 <= angle[i, j] < 112.5:
                    q = G[i+1, j]
                    r = G[i-1, j]
                elif 112.5 <= angle[i, j] < 157.5:
                    q = G[i-1, j-1]
                    r = G[i+1, j+1]
    
                if G[i, j] >= q and G[i, j] >= r:
                    Z[i, j] = G[i, j]
                else:
                    Z[i, j] = 0
            except IndexError:
                pass
    
    weak = 50
    strong = 255
    res = np.zeros_like(Z)
    strong_i, strong_j = np.where(Z >= high_threshold)
    weak_i, weak_j = np.where((Z <= high_threshold) & (Z >= low_threshold))
    res[strong_i, strong_j] = strong
    res[weak_i, weak_j] = weak
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if res[i, j] == weak:
                if ((res[i+1, j-1:j+2] == strong).any() or 
                    (res[i-1, j-1:j+2] == strong).any() or 
                    (res[i, [j-1, j+1]] == strong).any()):
                    res[i, j] = strong
                else:
                    res[i, j] = 0
    
    return res.astype(np.uint8)