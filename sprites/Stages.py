import pygame
import configs as cf


class StageOne(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/stage1.png")
        self.rect = self.image.get_rect()

        self.scaled = pygame.transform.scale(
            self.image,
            (cf.WINDOW_X, cf.WINDOW_Y)
        )
