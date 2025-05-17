import pygame
import configs as cf


class StageOne():

    # Constructor
    def __init__(self):
        self.image = pygame.image.load("sprites/stage1.png")

        self.scaled = pygame.transform.scale(
            self.image,
            (cf.WINDOW_X, cf.WINDOW_Y)
        )
