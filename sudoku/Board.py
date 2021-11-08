import pygame

pygame.font.init()


class Board:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.generated = True

    def draw(self, window):
        font = pygame.font.SysFont("comicsans", 40)
        temp = self.width / 9
        x = self.col * temp
        y = self.row * temp

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (255, 0, 0))
            window.blit(text, (x + (temp / 2 - text.get_width() / 2), y + (temp / 2 - text.get_height() / 2)))
        elif not (self.value == 0):
            if self.generated == False:
                text = font.render(str(self.value), 1, (104, 104, 104))
            else:
                text = font.render(str(self.value), 1, (60, 153, 102))
            window.blit(text, (x + (temp / 2 - text.get_width() / 2), y + (temp / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(window, (255, 100, 0), (x, y, temp, temp), 3)

    def draw_change(self, window):
        font = pygame.font.SysFont("comicsans", 40)
        temp = self.width / 9
        x = self.col * temp
        y = self.row * temp

        text = font.render(str(self.value), 1, (0, 0, 0))
        window.blit(text, (x + (temp / 2 - text.get_width() / 2), y + (temp / 2 - text.get_height() / 2)))

    def set_value(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val
