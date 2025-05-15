import pygame


class Alien(pygame.sprite.Sprite):
    moves = 0
    orig_x = 0
    
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/alien.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.orig_x = x # For resetting to initial pos on x axis
        self.rect.y = y
        
        
    def update(self):
        self.rect.x += 25
        self.moves += 1
        if self.moves == 3:
            self.rect.x = self.orig_x
            self.moves = 0


class Alienbullet(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/alienbullet.png")
        self.rect = self.image.get_rect()
        
        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y + (self.rect.height)
        
    
    def update(self):
        self.rect.y += 3