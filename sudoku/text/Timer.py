import pygame


def timer(time):
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Time: " + format_time(time), 1, (250, 35, 100))
    return text


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    return " " + str(minute) + ":" + str(sec)
