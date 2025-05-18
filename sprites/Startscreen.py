import pygame
from configs import *


class Startscreen(pygame.sprite.Sprite):

    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/startscreen.png")
        self.rect = self.image.get_rect()
        self.scaled = pygame.transform.scale(
            self.image,
            (WINDOW_X, WINDOW_Y)
        )


class StartButton(pygame.sprite.Sprite):
    spritesheet = pygame.image.load("sprites/startbuttonsheet.png")
    hover_rect = pygame.Rect(0, 0, 320, 118)
    no_hover_rect = pygame.Rect(320, 0, 320, 118)

    # Constructor
    def __init__(self):
        super().__init__()

        # Create surfaces
        self.hover = pygame.Surface(
            self.hover_rect.size,
            pygame.SRCALPHA
        ).convert_alpha()
        self.no_hover = pygame.Surface(
            self.no_hover_rect.size,
            pygame.SRCALPHA
        ).convert_alpha()
        # Draw on the surfaces
        self.hover.blit(self.spritesheet, (0, 0), self.hover_rect)
        self.no_hover.blit(self.spritesheet, (0, 0), self.no_hover_rect)

        self.image = self.no_hover  # Manages what surface to show
        self.rect = self.image.get_rect()
        self.rect.x = (WINDOW_X / 2) - (self.rect.width / 2)
        self.rect.y = (WINDOW_Y - self.rect.height - 100)

    def update(self, is_hover):
        if is_hover:
            self.image = self.hover
            return True
        else:
            self.image = self.no_hover
            return False
