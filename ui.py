import pygame
from settings import *

# In-Game Screens
def draw_play(screen, font, background, usb_img, monitor_img, monitor_hit, usb_hit):
    screen.blit(background, (0,0))
    screen.blit(monitor_img, monitor_hit)
    screen.blit(usb_img, usb_hit)

def draw_desktop(screen, font, day):
    screen.fill(DESKTOP)
    day_text = font.render(f"day {day}", True, WHITE)
    screen.blit(day_text, (20,20))

def draw_popup(screen, font):
    popup_rect = pygame.Rect(100,150,300,300)
    pygame.draw.rect(screen, BLACK, popup_rect)

    title = font.render("DOWNLOAD NOW!", True, WHITE)
    text = font.render("(Press R to reset)", True, WHITE)

    screen.blit(title,(110, 180))
    screen.blit(text,(110, 220))

def draw_scan(screen, font):
    title = font.render("Running system scannnnn.....", True, WHITE)
    text = font.render("(Press R to reset)", True, WHITE)

    screen.blit(title,(110, 180))
    screen.blit(text,(110, 220))


# UI Screens (Menu, Day Select, Tutorial)
def draw_menu(screen, font):
    screen.fill(BLACK)
    title = font.render(f"Cybersecurity Game", True, WHITE)
    text = font.render("(press enter to start)", True, WHITE)

    screen.blit(title, (120, 200)) 
    screen.blit(text, (120, 240))

def draw_dayselect(screen, font):
    screen.fill(BLACK)
    title = font.render(f"Select Day:", True, WHITE)

    screen.blit(title, (120, 170))
    for i in range(1,8):
        day_text = font.render(str(i), True, WHITE)
        screen.blit(day_text, (150 + i * 30, 200))

def draw_tutorial(screen,font):
    screen.fill(BLACK)
    lines = [
        "Tutorial Screen",
        "Line 2",
        "",
        "Press space to continue"
    ]
    y = 150
    for line in lines:
        text = font.render(line, True, WHITE)
        screen.blit(text, (50, y))
        y += 40
