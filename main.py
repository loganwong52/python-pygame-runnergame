# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons (I've done this already)
# run code in terminal with:   python3 main.py

import pygame
from image_helper import loadify
from sys import exit

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

# snail animation
snail_surface = loadify("./UltimatePygameIntro-main/graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

# player and Rectangle
player_surf = loadify("./UltimatePygameIntro-main/graphics/Player/player_walk_1.png")
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

# while loop needed to make pygame display window stay open forever
while True:
    # Find the specific event that lets users closer windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # the opposite of pygame.init()
            # Use exit so code outside the for loop won't run once you call quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     # only triggers if you move the mouse
        #     mouse_position = event.pos
        #     player_hit_mouse = player_rect.collidepoint(mouse_position)
        #     if player_hit_mouse:
        #         print("collision")
        # if event.type == pygame.MOUSEBUTTONUP:
        #     print("mouse up")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print("mouse down")

        if event.type == pygame.KEYDOWN:
            # print("key down")
            if event.key == pygame.K_SPACE:
                # print("jump")
                player_gravity = -20

        # if event.type == pygame.KEYUP:
        # print("key up")

    # Attach test_surface to the DISPLAY surface
    # BLock Image Transfer aka "blit" command
    # (0, 0) is the TOP LEFT corner of the window
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # .draw and specify shape. Takes in what to draw ON, color, what to draw
    # pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), width=10)
    pygame.draw.rect(screen, "#c0e8ec", score_rect)  # inner
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)  # boarder

    # Draw a circle from scratch
    # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))
    screen.blit(score_surf, score_rect)

    # Animate the snail to move left
    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)

    # PLAYER
    # Don't move the player surface, BUT RATHER, the rectangle containing the surface
    # player_rect.left += 1
    # print(player_rect.left)  # or print where the left edge of the player_rect is!
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surf, player_rect)

    # Keyboard input by using pygame.key
    # keys = pygame.key.get_pressed()
    # # a tuple with 0's or 1's if a button is pressed... a dictionary!
    # space_btn_pressed = keys[pygame.K_SPACE]
    # if space_btn_pressed:
    #     print("jump")

    # RECTANGLE COLLISIONS
    # returns 0 if no collision or 1 if collision
    # snail_hit_player = player_rect.colliderect(snail_rect)
    # if snail_hit_player:
    #     print("collision!")

    # MOUSE COLLISION
    # collidepoint() takes in a tuple (x, y), mouse_pos is a tuple
    # mouse_pos = pygame.mouse.get_pos()
    # player_hit_mouse = player_rect.collidepoint(mouse_pos)
    # if player_hit_mouse:
    #     # print("collision")
    #     mouse_btns_bools = pygame.mouse.get_pressed()
    #     # (left clicked?, middle clicked?, right clicked?)
    #     print(mouse_btns_bools)

    # draw all our elements; update everything.
    pygame.display.update()
    # frames per second ceiling: shouldn't run faster than 60 fps)
    clock.tick(60)
