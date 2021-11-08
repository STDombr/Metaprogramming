import pygame


def status(status):
    font = pygame.font.SysFont("comicsans", 40)
    if status == 1:
        text = font.render("You Won!", 1, (43, 255, 0))
    if status == 0:
        text = font.render("You Lose!", 1, (255, 0, 0))
    return text
