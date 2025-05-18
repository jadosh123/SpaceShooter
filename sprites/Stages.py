import pygame
from configs import *


class StageOne():

    # Constructor
    def __init__(self):
        self.image = pygame.image.load("sprites/stage1.png")

        self.scaled = pygame.transform.scale(
            self.image,
            (WINDOW_X, WINDOW_Y)
        )
