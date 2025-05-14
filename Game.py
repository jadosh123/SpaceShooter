# Example file showing a circle moving on screen
import pygame
from sprites.Spaceship import SpaceShip
WINDOW_X = 1280
WINDOW_Y = 800
RES_X = 320
RES_Y = 240

if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    game_surface = pygame.Surface((RES_X, RES_Y))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(
        game_surface.get_width() / 2,
        game_surface.get_height() / 1.2
    )

    # Sprite group to hold sprites
    all_sprites = pygame.sprite.Group()

    # Load spaceship sprite
    spaceship = SpaceShip(player_pos.x, player_pos.y, "sprites/spaceship.png")
    all_sprites.add(spaceship)

    while running:
        # poll for events pygame.QUIT event means
        # the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from
        # last frame
        game_surface.fill("black")

        all_sprites.draw(game_surface)

        keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
        #     player_pos.y -= 300 * dt
        # if keys[pygame.K_s]:
        #     player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            if player_pos.x > 10:
                player_pos.x -= 10
                spaceship.update_pos_x(player_pos.x)
        if keys[pygame.K_d]:
            if player_pos.x < RES_X - 10 - spaceship.rect.width:
                player_pos.x += 10
                spaceship.update_pos_x(player_pos.x)
        if keys[pygame.K_j]:
            # TODO Implement shooting lasers
            pass

        scaled_surface = pygame.transform.scale(
            game_surface,
            (WINDOW_X, WINDOW_Y)
        )

        screen.blit(scaled_surface, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60 dt is delta time in seconds since
        # last frame, used for framerate-independent physics.
        dt = clock.tick(60)

    pygame.quit()
