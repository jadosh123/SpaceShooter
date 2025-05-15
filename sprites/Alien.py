import pygame


class Alien(pygame.sprite.Sprite):
    
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/alien.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        pass