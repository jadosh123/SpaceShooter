import pygame
import configs as cf


class Startscreen(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/startscreen.png")
        self.rect = self.image.get_rect()
        self.scaled = pygame.transform.scale(
            self.image,
            (cf.WINDOW_X, cf.WINDOW_Y)
        )


class StartButton(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/startbutton.png")
        self.rect = self.image.get_rect()
        self.scaled = pygame.transform.scale(
            self.image,
            (320, 120)
        )
