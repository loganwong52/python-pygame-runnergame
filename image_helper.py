import pygame


def loadify(imgname):
    return pygame.image.load(imgname).convert_alpha()
