# helpers.py

import pygame
import sys


def load_sprite(path, size, position):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, size)
    hitbox = img.get_rect(topleft=position)
    mask = pygame.mask.from_surface(img)
    return img, hitbox, mask