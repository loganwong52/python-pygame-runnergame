import pygame
from image_helper import loadify
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        player_walk_1 = loadify(
            "./UltimatePygameIntro-main/graphics/Player/player_walk_1.png"
        )
        player_walk_2 = loadify(
            "./UltimatePygameIntro-main/graphics/Player/player_walk_2.png"
        )
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = loadify(
            "./UltimatePygameIntro-main/graphics/Player/jump.png"
        )

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound(
            "./UltimatePygameIntro-main/audio/jump.mp3"
        )
        self.jump_sound.set_volume(0.25)

    def player_input(self):
        """
        If space is pressed, the player moves up.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20

    def apply_gravity(self):
        """
        Player is always moving down, but won't fall below ground.
        """
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):
        """
        Animate player jumping if not on the ground.
        Or animate player walking if on the ground.
        """
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        """
        The only "public" function here besides init().
        Called in main.py
        """
        self.player_input()
        self.apply_gravity()
        self.animation_state()
