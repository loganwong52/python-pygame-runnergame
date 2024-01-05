# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons (I've done this already)
# run code in terminal with:   python3 main.py

import pygame
from image_helper import loadify
from sys import exit
from random import randint


def player_animation():
    """
    Display jump surface if not on floor
    Play walking animation if player is on floor
    """
    global player_surf, player_index
    if player_rect.bottom < 300:
        # jump
        player_surf = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index > len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]


def collisions(player, obstacles):
    """
    Checks if player collided with an obstacle
    """
    if obstacles:
        # Make every obstacle move left 5 spaces
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                # you want to set game_active to False...
                return False
    return True


def obstacle_movement(obstacle_list):
    """
    Controls all obstacle movement
    """
    if obstacle_list:
        # Make every obstacle move left 5 spaces
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        # Only save obstacles on screen
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 0]

        return obstacle_list
    return []


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


pygame.init()  # necessary
# set_mode needs a tuple: (width, height)
# CREATE DISPLAY SURFACE
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# Create the clock object for the framerate
clock = pygame.time.Clock()

# Create a font object
# None is default font_type
font_type = "./UltimatePygameIntro-main/font/Pixeltype.ttf"
font_size = 50
test_font = pygame.font.Font(font_type, font_size)

# Controls game states
game_active = False

# Player score
start_time = 0
score = 0

# SURFACE
# User sees all things on a surface
# Display surface: The game window (the actual canvas) aka screen
# Regular surface: a single image that needs the display surface for the user to see it (individual images on the canvas)

# EXAMPLE REGULAR SURFACE
# w = 100
# h = 200
# test_surface = pygame.Surface((w, h))
# test_surface.fill("Red")

# REGULAR SURFACES WITH IMAGE
sky_surface = loadify("./UltimatePygameIntro-main/graphics/Sky.png")
ground_surface = loadify("./UltimatePygameIntro-main/graphics/ground.png")

# CREATING TEXT
# 1. Create a font  2. write text on a surface   3. blit that surface
text = "Logan's Game"
anti_alias = False  # looks pixelated or smooth
# text_color = "black"
text_color = (64, 64, 64)
# text_surf = test_font.render(text, anti_alias, text_color)
score_surf = test_font.render(text, anti_alias, text_color)
score_rect = score_surf.get_rect(center=(400, 50))

# Start screen title
game_title_surf = test_font.render("Runner Game", False, (111, 196, 169))
game_title_rect = game_title_surf.get_rect(center=(400, 80))

# Start screen score
game_msg = test_font.render("Press space to start", False, (111, 196, 169))
game_msg_rect = game_msg.get_rect(center=(400, 320))

# player, animation, and Rectangle
player_walk_1 = loadify("./UltimatePygameIntro-main/graphics/Player/player_walk_1.png")
player_walk_2 = loadify("./UltimatePygameIntro-main/graphics/Player/player_walk_2.png")
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = loadify("./UltimatePygameIntro-main/graphics/Player/jump.png")

player_surf = player_walk[player_index]
player_x = 80
player_y = 300
player_rect = player_surf.get_rect(
    midbottom=(player_x, player_y)
)  # draw rectangle around player
# surfaces place object according to top left corner
# rectangles let you specify where to place which dot where
# top left corner, mid top, top right corner
# left, center, right
# bottom left corner, mid bottom, bottom right corner

# PYGAME.DRAW
# draw shapes, lines, or points

# PLAYER GRAVITY
player_gravity = 0


# Start/game over page
player_stand = loadify("./UltimatePygameIntro-main/graphics/Player/player_stand.png")
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))


# Timer for OBSTACLES
obstacle_timer = pygame.USEREVENT + 1
# Takes 2 args: the event, and how often to trigger it in ms
pygame.time.set_timer(obstacle_timer, 1500)
# create list of obstacles
# when event is triggered, it creates a new obstacle rectangle
# move the rectangle left on every frame

# snail animation
snail_surf = loadify("./UltimatePygameIntro-main/graphics/snail/snail1.png")
fly_surf = loadify("./UltimatePygameIntro-main/graphics/Fly/Fly1.png")

obstacle_rect_list = []

# while loop needed to make pygame display window stay open forever
while True:
    # Find the specific event that lets users closer windows
    # THE EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # the opposite of pygame.init()
            # Use exit so code outside the for loop won't run once you call quit()
            exit()

        if game_active:
            # Player jumps if Mouse clicks on him
            # collidepoint() takes in a tuple (x, y), mouse_pos is a tuple
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_hit_mouse = player_rect.collidepoint(event.pos)
                if player_hit_mouse and player_rect.bottom >= 300:
                    player_gravity = -20

            # Player jumps is space bar is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20

            # if event.type == pygame.KEYUP:
            # print("key up")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                # x-value should be between 900 and 1100
                obstacle_rect_list.append(
                    snail_surf.get_rect(bottomright=(randint(900, 1100), 300))
                )
            else:
                obstacle_rect_list.append(
                    fly_surf.get_rect(bottomright=(randint(900, 1100), 210))
                )

    if game_active:
        # Attach test_surface to the DISPLAY surface
        # BLock Image Transfer aka "blit" command
        # (0, 0) is the TOP LEFT corner of the window
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # Animate the snail to move left
        # snail_rect.x -= 4
        # if snail_rect.right < 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # PLAYER
        # Don't move the player surface, BUT RATHER, the rectangle containing the surface
        # player_rect.left += 1
        # print(player_rect.left)  # or print where the left edge of the player_rect is!
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        # OBSTACLE COLLISIONS
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # RECTANGLE COLLISIONS
        # returns 0 if no collision or 1 if collision
        # snail_hit_player = player_rect.colliderect(snail_rect)
        # if snail_hit_player:
        # game_active = False
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        # Populate start/game over screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)
        obstacle_rect_list.clear()  # remove all obstacles
        player_rect.midbottom = (80, 300)  # ensure player starts on ground
        player_gravity = 0

        # Show instructions if score is 0, otherwise show the score
        score_msg = test_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_msg_rect = score_msg.get_rect(center=(400, 330))
        if score == 0:
            screen.blit(game_msg, game_msg_rect)
        else:
            screen.blit(score_msg, score_msg_rect)

    # draw all our elements; update everything.
    pygame.display.update()
    # frames per second ceiling: shouldn't run faster than 60 fps)
    clock.tick(60)
