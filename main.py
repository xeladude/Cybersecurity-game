# main.py

import pygame
import sys

from settings import *
from ui import draw_desktop, draw_popup, draw_scan, draw_menu, draw_dayselect, draw_tutorial, draw_play
from helpers import *


def main():
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption(TITLE)

    bg = pygame.image.load("assets\\backgrounds\\Bgpisckel-1.png").convert()
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))

    monitor_img, monitor_hit, monitor_mask = load_sprite("assets\\objects\\monitor.png", (760, 380), (10, 10))
    usb_img, usb_hit, usb_mask = load_sprite("assets\\objects\\usb.png", (186, 88), (10, 340))



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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if game_state == STATE_PLAY:
                    if monitor_hit.collidepoint(mouse_pos):
                        rel_x = mouse_pos[0] - monitor_hit.x
                        rel_y = mouse_pos[1] - monitor_hit.y
                        if monitor_mask.get_at((rel_x, rel_y)):
                            print("monitor clicked")
                    elif usb_hit.collidepoint(mouse_pos):
                        rel_x = mouse_pos[0] - usb_hit.x
                        rel_y = mouse_pos[1] - usb_hit.y
                        if usb_mask.get_at((rel_x, rel_y)):
                            print("usb clicked")





        # Drawing
        # screen.fill(DESKTOP)

        if game_state == STATE_MENU:
            draw_menu(screen, font)
        
        elif game_state == STATE_DAY_SELECT:
            draw_dayselect(screen, font)

        elif game_state == STATE_TUTORIAL:
            draw_tutorial(screen, font)

        elif game_state == STATE_PLAY:
            draw_play(screen, font, bg, usb_img, monitor_img, monitor_hit, usb_hit)

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