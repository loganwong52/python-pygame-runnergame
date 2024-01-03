# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons (I've done this already)
# run code in terminal with:   python3 main.py

import pygame
from sys import exit

pygame.init()  # necessary
# set_mode needs a tuple: (width, height)
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")

# Create the clock object for the framerate
clock = pygame.time.Clock()

# SURFACE
# User sees all things on a surface
# Display surface: The game window (the actual canvas)
# Regular surface: a single image that needs the display surface for the user to see it (individual images on the canvas)

# EXAMPLE REGULAR SURFACE
# w = 100
# h = 200
# test_surface = pygame.Surface((w, h))
# test_surface.fill("Red")

# REGULAR SURFACE WITH IMAGE
sky_surface = pygame.image.load("./UltimatePygameIntro-main/graphics/Sky.png")
ground_surface = pygame.image.load("./UltimatePygameIntro-main/graphics/ground.png")

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

        # draw all our elements
        # update everything.
        pygame.display.update()

        # This while true loop shouldn't run faster than 60 frames per second (a ceiling)
        clock.tick(60)
