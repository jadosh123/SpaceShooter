import pygame


class SpaceShip(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y, file_path):
        super().__init__()
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update_pos_x(self, x):
        self.rect.x = x
