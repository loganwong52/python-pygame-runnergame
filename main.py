# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons (I've done this already)
# run code in terminal with:   python3 main.py

import pygame
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
sky_surface = pygame.image.load("./UltimatePygameIntro-main/graphics/Sky.png")
ground_surface = pygame.image.load("./UltimatePygameIntro-main/graphics/ground.png")

# CREATING TEXT
# 1. Create a font  2. write text on a surface   3. blit that surface
text = "Logan's Game"
anti_alias = False  # looks pixelated or smooth
text_color = "black"
text_surface = test_font.render(text, anti_alias, text_color)

# while loop needed to make pygame display window stay open forever
while True:
    # Find the specific event that lets users closer windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # the opposite of pygame.init()
            # Use exit so code outside the for loop won't run once you call quit()
            exit()

        # Attach test_surface to the DISPLAY surface
        # BLock Image Transfer aka "blit" command
        # (0, 0) is the TOP LEFT corner of the window
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))

        # draw all our elements
        # update everything.
        pygame.display.update()

        # This while true loop shouldn't run faster than 60 frames per second (a ceiling)
        clock.tick(60)
