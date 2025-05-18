import pygame
from configs import *


class SpaceShip(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.orig_image = pygame.image.load(
            "sprites/spaceship.png").convert_alpha()
        self.rect = self.orig_image.get_rect()
        scale_x = WINDOW_X / RES_X
        scale_y = WINDOW_Y / RES_Y
        new_width = self.rect.width * scale_x
        new_height = self.rect.height * scale_y
        self.image = pygame.transform.scale(
            self.orig_image,
            (new_width, new_height)
        )
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self, x):
        self.rect.x = x


class Playerbullet(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y):
        super().__init__()
        self.orig_image = (
            pygame.image.load("sprites/shipbullet.png").convert_alpha()
        )
        self.rect = self.orig_image.get_rect()
        scale_x = WINDOW_X / RES_X
        scale_y = WINDOW_Y / RES_Y
        new_width = self.rect.width * scale_x
        new_height = self.rect.height * scale_y
        self.image = pygame.transform.scale(
            self.orig_image,
            (new_width, new_height)
        )
        self.rect = self.image.get_rect()

        self.rect.x = x - (self.rect.width / 2)
        self.rect.y = y

    def update(self):
        self.rect.y -= 10
