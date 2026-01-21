# main.py

import pygame
import sys

from settings import *
from ui import draw_desktop, draw_popup, draw_scan, draw_menu, draw_dayselect, draw_tutorial


def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()

    # Fonts
    font = pygame.font.SysFont("arial",20)

    # Game State
    running = True
    current_day = START_DAY
    game_state = STATE_MENU
    
    while running: 
        clock.tick(FPS)


        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # State specific inputs and updates
                # MENU -> DAY SELECT
                if game_state == STATE_MENU:
                    if event.key == pygame.K_RETURN:
                        game_state = STATE_DAY_SELECT

                # DAY SELECT -> TUTORIAL
                elif game_state == STATE_DAY_SELECT:
                    if event.key == pygame.K_1 <= event.key <= pygame.K_7:
                        current_day = event.key - pygame.K_0
                        if current_day == 1:
                            game_state = STATE_TUTORIAL
                        else:
                            game_state = STATE_DESKTOP


        # Drawing
        # screen.fill(DESKTOP)

        if game_state == STATE_MENU:
            draw_menu(screen, font)
        
        elif game_state == STATE_DAY_SELECT:
            draw_dayselect(screen, font)

        elif game_state == STATE_TUTORIAL:
            draw_tutorial(screen, font)


        elif game_state == STATE_DESKTOP:
            draw_desktop(screen, font, current_day)

        elif game_state == STATE_POPUP:
            draw_popup(screen, font)

        elif game_state == STATE_SCAN:
            draw_scan(screen, font)


        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()