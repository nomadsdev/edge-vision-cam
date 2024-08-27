import pygame

class DisplayHandler:
    def __init__(self, resolution=(1280, 720), caption="Camera"):
        pygame.display.init()
        self.screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
    
    def update_display(self, surface):
        self.screen.blit(surface, (0, 0))
        pygame.display.update()