# Example file showing a circle moving on screen
import pygame
import random
import configs as cf
from utils import collision_detection, mouse_hovering
from sprites.Spaceship import SpaceShip, Playerbullet
from sprites.Alien import Alien, Alienbullet
from sprites.Startscreen import Startscreen, StartButton
from sprites.Stages import StageOne


def init_game_sprites(
    alien_sprites,
    player_ship,
    spaceship,
    player_projectiles,
    alien_projectiles
):
    alien_sprites.empty()
    player_ship.empty()
    player_projectiles.empty()
    alien_projectiles.empty()

    # Load aliens
    for i in range(5):
        for j in range(3):
            alien_sprites.add(Alien(60 + i * 220, 25 + j * 120))

    player_ship.add(spaceship)
    return


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((cf.WINDOW_X, cf.WINDOW_Y))
    start_screen = Startscreen()
    start_button = StartButton()
    stage_one = StageOne()
    clock = pygame.time.Clock()
    running = True
    dt = 0
    last_player_ship_bullet = 0  # Tracks time since last shot
    last_alien_time = 0  # Tracks time since last pos
    last_alien_bullet = 0  # Tracks time since last shot
    is_start_screen = True
    is_reset_game = False

    player_ship_pos = pygame.Vector2(
        stage_one.scaled.get_width() / 2,
        stage_one.scaled.get_height() / 1.2
    )

    # Sprite group to hold sprites
    player_ship = pygame.sprite.Group()
    alien_projectiles = pygame.sprite.Group()
    player_ship_projectiles = pygame.sprite.Group()
    alien_sprites = pygame.sprite.Group()
    start_sprites = pygame.sprite.Group()

    start_sprites.add(start_button)

    # Load spaceship sprite
    spaceship = SpaceShip(player_ship_pos.x, player_ship_pos.y)
    init_game_sprites(
        alien_sprites,
        player_ship,
        spaceship,
        player_ship_projectiles,
        alien_projectiles
    )

    # Copy stage map
    scaled_stage_copy = stage_one.scaled.copy()

    while running:
        # Check to reset game state
        if is_reset_game:
            init_game_sprites(
                alien_sprites,
                player_ship,
                spaceship,
                player_ship_projectiles,
                alien_projectiles
            )
            is_reset_game = False
            is_start_screen = True

        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        mouse_click = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        # poll for events pygame.QUIT event means
        # the user clicked X to close your window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Displays start screen else displays game
        if is_start_screen:
            start_sprites.draw(start_screen.scaled)
            screen.blit(start_screen.scaled, (0, 0))
            # Temporary for start screen
            if mouse_hovering(mouse_pos, start_button):
                if mouse_click[0]:
                    is_start_screen = False
        else:
            # Check game state
            if (not alien_sprites) or (not player_ship):
                is_reset_game = True
                continue

            # fill the screen with a color to wipe away anything from
            # last frame
            stage_one.scaled.fill((0, 0, 0))
            stage_one.scaled.blit(scaled_stage_copy, (0, 0))

            player_ship.draw(stage_one.scaled)
            alien_sprites.draw(stage_one.scaled)
            # Move player_ship left
            if keys[pygame.K_a]:
                if player_ship_pos.x > 10:
                    player_ship_pos.x -= cf.SHIP_SPEED
                    spaceship.update(player_ship_pos.x)
            # Move player_ship right
            if keys[pygame.K_d]:
                if player_ship_pos.x < cf.WINDOW_X - 10 - spaceship.rect.width:
                    player_ship_pos.x += cf.SHIP_SPEED
                    spaceship.update(player_ship_pos.x)
            # player_ship projectiles
            if (
                keys[pygame.K_j]
                and
                current_time - last_player_ship_bullet > 500
            ):
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
                if sprite.rect.y + sprite.rect.height >= cf.WINDOW_Y:
                    sprite.kill()

            for sprite in player_ship_projectiles:
                if sprite.rect.y <= 0:
                    sprite.kill()

            alien_projectiles.draw(stage_one.scaled)
            player_ship_projectiles.draw(stage_one.scaled)

            # Display game surface on main screen
            screen.blit(stage_one.scaled, (0, 0))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60 dt is delta time in seconds since
        # last frame, used for framerate-independent physics.
        dt = clock.tick(60)

    pygame.quit()
