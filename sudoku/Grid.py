import pygame
from Board import Board

from text.Status import status
from text.Timer import timer

pygame.font.init()


class Grid:

    def __init__(self, board, rows, cols, width, height, window, timer):
        self.rows = rows
        self.cols = cols
        self.board = [[Board(board[i][j], i, j, width, height) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.window = window
        self.timer = timer
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col].value == 0:
                    self.board[row][col].generated = False

    def update_model(self):
        self.model = [[self.board[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def restore_fields(self, window):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].generated == False:
                    self.board[i][j].value = 0
                    self.board[i][j].temp = 0
                    self.model[i][j] = 0

    def restore_generated(self, window):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].generated == False:
                    self.board[i][j].generated = True

    def place(self, val):
        row, col = self.selected
        if self.board[row][col].value == 0:
            self.board[row][col].set_value(val)
            self.update_model()

    def set_temp(self, val):
        row, col = self.selected
        self.board[row][col].set_temp(val)

    def draw(self):
        temp = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.window, (50, 50, 50), (0, i * temp), (self.width, i * temp), thick)
            pygame.draw.line(self.window, (50, 50, 50), (i * temp, 0), (i * temp, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].draw(self.window)

    def select(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j].selected = False

        self.board[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.board[row][col].generated == False:
            if self.board[row][col].value == 0:
                self.board[row][col].set_temp(0)
            else:
                self.board[row][col].set_value(0)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            temp = self.width / 9
            x = pos[0] // temp
            y = pos[1] // temp
            return int(y), int(x)
        else:
            return None

    def find_empty(self):
        for i in range(len(self.model)):
            for j in range(len(self.model[0])):
                if self.model[i][j] == 0:
                    return i, j

        return None

    def find_not_generated(self):
        for i in range(len(self.model)):
            for j in range(len(self.model[0])):
                if self.board[i][j].generated == False:
                    return i, j

        return None

    def is_finished(self):
        if self.find_empty():
            return False
        return True


def redraw_window(window, grid):
    window.fill((240, 240, 240))

    temp = grid.width / 9
    for row in range(0, 9):
        for col in range(0, 9):
            if grid.board[row][col].generated == False:
                pygame.draw.rect(window, (145, 255, 145), (temp * col, temp * row, temp, temp))
    grid.draw()


def update_time(window, grid, time):
    if not grid.is_finished():
        text = timer(time)
        window.blit(text, (160, 560))


def check_solution(self):
    for row in range(self.rows):
        for col in range(self.cols):
            pos = (row, col)
            num = self.model[pos[0]][pos[1]]
            # Check row
            for i in range(len(self.model[0])):
                if self.model[pos[0]][i] == num and pos[1] != i:
                    return False

            # Check column
            for i in range(len(self.model)):
                if self.model[i][pos[1]] == num and pos[0] != i:
                    return False

            # Check box
            box_x = pos[1] // 3
            box_y = pos[0] // 3

            for i in range(box_y * 3, box_y * 3 + 3):
                for j in range(box_x * 3, box_x * 3 + 3):
                    if self.model[i][j] == num and (i, j) != pos:
                        return False

    return True


def victory(window):
    text = status(1)
    window.blit(text, (160, 560))


def fail(window):
    text = status(0)
    window.blit(text, (160, 560))
