# Example file showing a circle moving on screen
import pygame
import random
from sprites.Spaceship import *
from sprites.Alien import *
WINDOW_X = 1280
WINDOW_Y = 800
RES_X = 320
RES_Y = 240
PLAYER_SPEED = 2.4


def collision_detection(entity_list, proj_list):
    x_collision = False
    y_collision = False
    
    for entity in entity_list:
        for projectile in proj_list:
            # Ranges for each projectile and entity
            proj_start_x = projectile.rect.x
            proj_end_x = projectile.rect.x + projectile.rect.width
            proj_start_y = projectile.rect.y
            proj_end_y = projectile.rect.y + projectile.rect.height
            ent_start_x = entity.rect.x
            ent_end_x = entity.rect.x + entity.rect.width
            ent_start_y = entity.rect.y
            ent_end_y = entity.rect.y + entity.rect.height
            
            # Check for horizontal overlap in bounding boxes x and y        
            if (
                proj_start_x >= ent_start_x and proj_start_x <= ent_end_x
                or
                proj_end_x >= ent_start_x and proj_end_x <= ent_end_x
                or
                proj_start_x <= ent_start_x and proj_end_x >= ent_end_x
            ):
                x_collision = True
                
            if (
                proj_start_y >= ent_start_y and proj_start_y <= ent_end_y
                or
                proj_end_y >= ent_start_y and proj_end_y <= ent_end_y
                or
                proj_start_y <= ent_start_y and proj_end_y >= ent_end_y
            ):
                y_collision = True
            
            if x_collision and y_collision:
                projectile.kill()
                entity.kill()
            else:
                x_collision = False
                y_collision = False
            


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    game_surface = pygame.Surface((RES_X, RES_Y))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    last_player_bullet = 0  # Tracks time since last shot
    last_alien_time = 0  # Tracks time since last pos
    last_alien_bullet = 0  # Tracks time since last shot
    
    player_pos = pygame.Vector2(
        game_surface.get_width() / 2,
        game_surface.get_height() / 1.2
    )

    # Sprite group to hold sprites
    player = pygame.sprite.Group()
    alien_projectiles = pygame.sprite.Group()
    player_projectiles = pygame.sprite.Group()
    alien_sprites = pygame.sprite.Group()

    # Load spaceship sprite
    spaceship = SpaceShip(player_pos.x, player_pos.y)
    player.add(spaceship)
    
    # Load aliens
    for i in range(5):
        for j in range(3):
            alien_sprites.add(Alien(15 + i * 50,5 + j * 30))

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

        player.draw(game_surface)
        alien_sprites.draw(game_surface)

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
        if keys[pygame.K_j] and current_time - last_player_bullet > 500:
            player_projectiles.add(
                Playerbullet(
                    player_pos.x + (spaceship.rect.width / 2), 
                    player_pos.y
                )
            )
            last_player_bullet = current_time  # Update to last created bullet in milliseconds

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


        # Check for collision player on enemy or reverse
        collision_detection(alien_sprites, player_projectiles)
        collision_detection(player, alien_projectiles)

        # Check if bullets reached end of bounds
        alien_projectiles.update()
        player_projectiles.update()
        for sprite in alien_projectiles:
            if sprite.rect.y + sprite.rect.height >= RES_Y:
                sprite.kill()
        
        for sprite in player_projectiles:
            if sprite.rect.y <= 0:
                sprite.kill()
            
        alien_projectiles.draw(game_surface)
        player_projectiles.draw(game_surface)

        # Scale game_surface to support lower res on bigger screen
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
