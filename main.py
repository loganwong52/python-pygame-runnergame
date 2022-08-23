# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

# Create the clock object for the framerate
clock = pygame.time.Clock()

# SURFACE
# User sees all things on a surface
# Display surface: The game window (the actual canvas)
# Regular surface: a single image that needs the display surface for the user to see it (individual images on the canvas)

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Use exit so code outside the for loop won't run once you call quit()
            exit()


        # block image transfer
        # (0, 0) is the TOP LEFT corner of the window
        screen.blit(test_surface, (200, 100))

        # draw all our elements
        # update everything.
        pygame.display.update()

        # This while true loop shouldn't run faster than 60 frames per second (a ceiling)
        clock.tick(60)