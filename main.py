import pygame
import pygame.transform
import pygame.surfarray
from camera_handler import CameraHandler
from display_handler import DisplayHandler
from edge_detection import detect_edges

def main():
    pygame.init()
    
    camera = CameraHandler((1280, 720))
    camera.start()
    
    display = DisplayHandler((1280, 720), "Enhanced Edge Detection Camera")
    
    clock = pygame.time.Clock()
    
    try:
        while True:
            img = camera.get_image()
            
            ed = detect_edges(img, sigma=1.5, low_threshold=50, high_threshold=150)
            
            sf = pygame.surfarray.make_surface(ed)
            sf = pygame.transform.rotate(sf, -90)
            sf = pygame.transform.flip(sf, True, False)
            
            display.update_display(sf)
            
            clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt
            
    except KeyboardInterrupt:
        camera.stop()
        pygame.quit()

if __name__ == "__main__":
    main()