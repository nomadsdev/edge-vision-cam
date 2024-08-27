import pygame
import pygame.camera

class CameraHandler:
    def __init__(self, resolution=(1280, 720)):
        pygame.camera.init()
        self.cameras = pygame.camera.list_cameras()
        if not self.cameras:
            raise ValueError("No camera found!")
        self.camera = pygame.camera.Camera(self.cameras[0], resolution)
    
    def start(self):
        self.camera.start()
    
    def stop(self):
        self.camera.stop()
    
    def get_image(self):
        return self.camera.get_image()