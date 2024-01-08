import pygame
from image_helper import loadify
from sys import exit
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        self.type = type
        if self.type == "snail":
            snail_1 = loadify("./UltimatePygameIntro-main/graphics/snail/snail1.png")
            snail_2 = loadify("./UltimatePygameIntro-main/graphics/snail/snail2.png")
            self.frames = [snail_1, snail_2]
            y_pos = 300

        else:
            fly_1 = loadify("./UltimatePygameIntro-main/graphics/Fly/Fly1.png")
            fly_2 = loadify("./UltimatePygameIntro-main/graphics/Fly/Fly2.png")
            self.frames = [fly_1, fly_2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        """
        Animates the snail or the fly
        """
        if self.type == "snail":
            self.animation_index += 0.05
        else:
            self.animation_index += 0.25

        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        """
        If the sprite goes too far left off screen, destroy it.
        """
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        """
        The only "public" function here besides init().
        Called in main.py
        """
        self.animation_state()
        self.rect.x -= 6
