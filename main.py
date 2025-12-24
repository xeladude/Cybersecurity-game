# main.py

import pygame
import sys

from settings import *

def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    # Fonts
    font = pygame.font.SysFont("arial",20)

    # Game State
    running = True
    current_day = START_DAY
    
    while running: 
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Drawing
        screen.fill(DESKTOP)
