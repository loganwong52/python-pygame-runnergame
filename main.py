# Needs to use bash
# in bash, pip install pygame
# then, press green triangle run buttons
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # Use exit so code outside the for loop won't run once you call quit()
            exit()

        # draw all our elements
        # update everything.
        pygame.display.update()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
