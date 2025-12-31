import pygame
from settings import *

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