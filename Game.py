# Example file showing a circle moving on screen
import pygame
import random
import configs as cf
from utils import collision_detection
from sprites.Spaceship import SpaceShip, Playerbullet
from sprites.Alien import Alien, Alienbullet
from sprites.Startscreen import Startscreen, StartButton

player_ship_SPEED = 2.4


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((cf.WINDOW_X, cf.WINDOW_Y))
    game_surface = pygame.Surface((cf.RES_X, cf.RES_Y))
    start_screen = Startscreen()
    start_button = StartButton()
    clock = pygame.time.Clock()
    running = True
    dt = 0
    last_player_ship_bullet = 0  # Tracks time since last shot
    last_alien_time = 0  # Tracks time since last pos
    last_alien_bullet = 0  # Tracks time since last shot
    is_start_screen = True

    player_ship_pos = pygame.Vector2(
        game_surface.get_width() / 2,
        game_surface.get_height() / 1.2
    )

    # Sprite group to hold sprites
    player_ship = pygame.sprite.Group()
    alien_projectiles = pygame.sprite.Group()
    player_ship_projectiles = pygame.sprite.Group()
    alien_sprites = pygame.sprite.Group()

    # Load spaceship sprite
    spaceship = SpaceShip(player_ship_pos.x, player_ship_pos.y)
    player_ship.add(spaceship)

    # Load aliens
    for i in range(5):
        for j in range(3):
            alien_sprites.add(Alien(15 + i * 50, 5 + j * 30))

    while running:
        current_time = pygame.time.get_ticks()

        # poll for events pygame.QUIT event means
        # the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Displays start screen else displays game
        if is_start_screen:
            btn_width = start_button.scaled.get_width()
            scaled_btn_x = (cf.WINDOW_X / 2) - (btn_width / 2)
            btn_height = start_button.scaled.get_height()
            scaled_btn_y = (cf.WINDOW_Y - btn_height - 100)
            screen.blit(start_screen.scaled, (0, 0))
            screen.blit(start_button.scaled, (scaled_btn_x, scaled_btn_y))
        else:
            # fill the screen with a color to wipe away anything from
            # last frame
            game_surface.fill("black")

            player_ship.draw(game_surface)
            alien_sprites.draw(game_surface)

            keys = pygame.key.get_pressed()
            # Move player_ship left
            if keys[pygame.K_a]:
                if player_ship_pos.x > 10:
                    player_ship_pos.x -= player_ship_SPEED
                    spaceship.update(player_ship_pos.x)
            # Move player_ship right
            if keys[pygame.K_d]:
                if player_ship_pos.x < cf.RES_X - 10 - spaceship.rect.width:
                    player_ship_pos.x += player_ship_SPEED
                    spaceship.update(player_ship_pos.x)
            # player_ship projectiles
            if keys[pygame.K_j] and current_time - last_player_ship_bullet > 500:
                player_ship_projectiles.add(
                    Playerbullet(
                        player_ship_pos.x + (spaceship.rect.width / 2),
                        player_ship_pos.y
                    )
                )
                last_player_ship_bullet = current_time

            # Alien movement logic
            if current_time - last_alien_time > 1000:
                alien_sprites.update()
                last_alien_time = current_time

            # Alien firing logic
            if current_time - last_alien_bullet > 500:
                alien_list = alien_sprites.sprites()
                rand_alien = random.choice(alien_list)
                alien_projectiles.add(
                    Alienbullet(
                        rand_alien.rect.x + (rand_alien.rect.width / 2),
                        rand_alien.rect.y
                    )
                )
                last_alien_bullet = current_time

            # Check for collision player_ship on enemy or reverse
            collision_detection(alien_sprites, player_ship_projectiles)
            collision_detection(player_ship, alien_projectiles)

            # Check if bullets reached end of bounds
            alien_projectiles.update()
            player_ship_projectiles.update()
            for sprite in alien_projectiles:
                if sprite.rect.y + sprite.rect.height >= cf.RES_Y:
                    sprite.kill()

            for sprite in player_ship_projectiles:
                if sprite.rect.y <= 0:
                    sprite.kill()

            alien_projectiles.draw(game_surface)
            player_ship_projectiles.draw(game_surface)

            # Scale game_surface to support lower res on bigger screen
            scaled_surface = pygame.transform.scale(
                game_surface,
                (cf.WINDOW_X, cf.WINDOW_Y)
            )

            screen.blit(scaled_surface, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60 dt is delta time in seconds since
        # last frame, used for framerate-independent physics.
        dt = clock.tick(60)

    pygame.quit()
