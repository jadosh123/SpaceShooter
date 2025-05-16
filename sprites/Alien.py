import pygame
import configs as cf


class Alien(pygame.sprite.Sprite):
    moves = 0
    orig_x = 0

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.orig_image = pygame.image.load("sprites/alien.png")
        self.rect = self.orig_image.get_rect()
        scale_x = cf.WINDOW_X / cf.RES_X
        scale_y = cf.WINDOW_Y / cf.RES_Y
        new_width = self.rect.width * scale_x
        new_height = self.rect.height * scale_y
        self.image = pygame.transform.scale(
            self.orig_image,
            (new_width, new_height)
        )
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.orig_x = x  # For resetting to initial pos on x axis
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
        self.orig_image = pygame.image.load("sprites/alienbullet.png")
        self.rect = self.orig_image.get_rect()
        scale_x = cf.WINDOW_X / cf.RES_X
        scale_y = cf.WINDOW_Y / cf.RES_Y
        new_width = self.rect.width * scale_x
        new_height = self.rect.height * scale_y
        self.image = pygame.transform.scale(
            self.orig_image,
            (new_width, new_height)
        )
        self.rect = self.image.get_rect()

        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y + (self.rect.height)

    def update(self):
        self.rect.y += 3
