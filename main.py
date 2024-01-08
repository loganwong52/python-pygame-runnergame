# python imports
import pygame
from sys import exit
from random import randint, choice

# local imports
from image_helper import loadify
from player import Player
from obstacle import Obstacle


def collision_sprite():
    """
    player is a GroupSingle that is NOT a sprite
    pass in sprite that collides
    pass in Group of sprites that can be collided into
    pass in if the obstacle should be deleted or not
    """
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True):
        obstacle_group.empty()
        return False
    return True


def display_score():
    """
    Displays the time in seconds the player has been playing.
    This acts as the player's score.
    """
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


pygame.init()
# CREATE DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# Create the clock object for the framerate
clock = pygame.time.Clock()

# Create a font object
font_type = "./UltimatePygameIntro-main/font/Pixeltype.ttf"
font_size = 50
test_font = pygame.font.Font(font_type, font_size)

# Controls game states
game_active = False

# Player score
start_time = 0
score = 0

# Create GroupSingle for the player, initialize a player
player = pygame.sprite.GroupSingle()
player.add(Player())

# create Group for Obstacles
obstacle_group = pygame.sprite.Group()

# REGULAR SURFACES WITH IMAGE
sky_surface = loadify("./UltimatePygameIntro-main/graphics/Sky.png")
ground_surface = loadify("./UltimatePygameIntro-main/graphics/ground.png")

# CREATING TEXT
text = "Logan's Game"
anti_alias = False  # looks pixelated or smooth
text_color = (64, 64, 64)  # black
score_surf = test_font.render(text, anti_alias, text_color)
score_rect = score_surf.get_rect(center=(400, 50))

# Start screen title
game_title_surf = test_font.render("Runner Game", False, (111, 196, 169))
game_title_rect = game_title_surf.get_rect(center=(400, 80))

# Start screen score
game_msg = test_font.render("Press space to start", False, (111, 196, 169))
game_msg_rect = game_msg.get_rect(center=(400, 320))

# Start/game over page
player_stand = loadify("./UltimatePygameIntro-main/graphics/Player/player_stand.png")
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))


# Timers for OBSTACLES
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)
fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

# obstacle list and choices
choices = ["fly", "snail", "snail", "snail"]

# while loop makes game window stay open
while True:
    # THE EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            # Spawn obstacles according to timer
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(choices)))
        else:
            # Let space bar start a new game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # Attach test_surface to the DISPLAY surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # PLAYER
        player.draw(screen)
        player.update()

        # OBSTACLE
        obstacle_group.draw(screen)
        obstacle_group.update()

        # COLLISIONS
        game_active = collision_sprite()

    else:
        # Populate start/game over screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)

        # Show instructions if score is 0, otherwise show the score
        score_msg = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_msg_rect = score_msg.get_rect(center=(400, 330))
        if score == 0:
            screen.blit(game_msg, game_msg_rect)
        else:
            screen.blit(score_msg, score_msg_rect)

    # draw all our elements; update everything.
    pygame.display.update()
    clock.tick(60)
