# main.py

import pygame
import sys

from settings import *
from ui import draw_desktop, draw_popup, draw_scan, draw_menu, draw_dayselect, draw_tutorial, draw_play



def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption(TITLE)

    bg = pygame.image.load("assets\\backgrounds\\Bgpisckel-1.png").convert()
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

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
            
            # elif event.type == pygame.VIDEORESIZE:
            #     current_width, current_height = event.size
            #     screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)

            elif event.type == pygame.KEYDOWN:
                # State specific inputs and updates
                
                # MENU -> DAY SELECT
                if game_state == STATE_MENU:
                    if event.key == pygame.K_RETURN:
                        game_state = STATE_DAY_SELECT

                # DAY SELECT -> TUTORIAL
                elif game_state == STATE_DAY_SELECT:
                    if pygame.K_1 <= event.key <= pygame.K_7:
                        current_day = event.key - pygame.K_0
                        if current_day == 1:
                            game_state = STATE_TUTORIAL
                        else:
                            game_state = STATE_PLAY

                # TUTORIAL -> PLAY (continue to desk)
                elif game_state == STATE_TUTORIAL:
                    print("Game state is = ")
                    print(STATE_MENU)
                    if event.key == pygame.K_RETURN:
                        print("Key pressed, switching to Play")
                        game_state = STATE_PLAY
                        print(STATE_MENU)



        # Drawing
        # screen.fill(DESKTOP)

        if game_state == STATE_MENU:
            draw_menu(screen, font)
        
        elif game_state == STATE_DAY_SELECT:
            draw_dayselect(screen, font)

        elif game_state == STATE_TUTORIAL:
            draw_tutorial(screen, font)

        elif game_state == STATE_PLAY:
            draw_play(screen, font, bg)

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