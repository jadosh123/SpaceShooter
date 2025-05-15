import pygame


class SpaceShip(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self, x):
        self.rect.x = x
        
        
class Playerbullet(pygame.sprite.Sprite):
    
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/shipbullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y


    def update(self):
        self.rect.y -= 3
        