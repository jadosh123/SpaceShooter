# Example file showing a circle moving on screen
import pygame
from sprites.Spaceship import *
from sprites.Alien import *
WINDOW_X = 1280
WINDOW_Y = 800
RES_X = 320
RES_Y = 240
PLAYER_SPEED = 2.4


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    game_surface = pygame.Surface((RES_X, RES_Y))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    plyr_bullet_time = 0
    
    player_pos = pygame.Vector2(
        game_surface.get_width() / 2,
        game_surface.get_height() / 1.2
    )

    # Sprite group to hold sprites
    all_sprites = pygame.sprite.Group()
    projectile_sprites = pygame.sprite.Group()

    # Load spaceship sprite
    spaceship = SpaceShip(player_pos.x, player_pos.y)
    all_sprites.add(spaceship)
    
    for i in range(5):
        all_sprites.add(Alien(i * 30, 0))

    while running:
        current_time = pygame.time.get_ticks()
        
        # poll for events pygame.QUIT event means
        # the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from
        # last frame
        game_surface.fill("black")

        # rect = spaceship.rect
        # pygame.draw.rect(game_surface, "yellow", rect)
        all_sprites.draw(game_surface)

        keys = pygame.key.get_pressed()
        # Move player left
        if keys[pygame.K_a]:
            if player_pos.x > 10:
                player_pos.x -= PLAYER_SPEED
                spaceship.update(player_pos.x)
        # Move player right
        if keys[pygame.K_d]:
            if player_pos.x < RES_X - 10 - spaceship.rect.width:
                player_pos.x += PLAYER_SPEED
                spaceship.update(player_pos.x)
        # Player projectiles
        if keys[pygame.K_j] and current_time - plyr_bullet_time > 500:
            projectile_sprites.add(
                Playerbullet(
                    player_pos.x + (spaceship.rect.width / 2), 
                    player_pos.y
                )
            )
            plyr_bullet_time = current_time  # Update to last created bullet in milliseconds

        # Constant position update for bullets
        projectile_sprites.update()
        for sprite in projectile_sprites:
            if sprite.rect.y >= RES_Y:
                sprite.kill()
            
        projectile_sprites.draw(game_surface)

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
