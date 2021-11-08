import copy
from random import shuffle


class SudokuGenerator:

    def __init__(self, empty_squares):
        self.counter = 0
        self.path = []
        self.board = [[0 for i in range(9)] for j in range(9)]

        self.generate_full_sudoku(self.board)
        self.remove_numbers(empty_squares)

        self.original = copy.deepcopy(self.board)

    def check_value(self, grid, row, col, number):
        if number in grid[row]:
            return False

        for i in range(9):
            if grid[i][col] == number:
                return False

        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        for i in range(sub_row, (sub_row + 3)):
            for j in range(sub_col, (sub_col + 3)):
                if grid[i][j] == number:
                    return False

        return True

    def solve_sudoku(self, grid):
        for i in range(0, 81):
            row = i // 9
            col = i % 9

            if grid[row][col] == 0:
                for number in range(1, 10):
                    # check that the number hasn't been used in the row/col/subgrid
                    if self.check_value(grid, row, col, number):
                        grid[row][col] = number
                        if not self.find_empty_square(grid):
                            self.counter += 1
                            break
                        else:
                            if self.solve_sudoku(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def generate_full_sudoku(self, grid):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            row = i // 9
            col = i % 9
            if grid[row][col] == 0:
                shuffle(number_list)
                for number in number_list:
                    if self.check_value(grid, row, col, number):
                        self.path.append((number, row, col))
                        grid[row][col] = number
                        if not self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_full_sudoku(grid):
                                return True
                break
        grid[row][col] = 0
        return False

    def find_empty_square(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i, j)
        return

    def get_non_empty_squares(self, grid):
        non_empty_squares = []
        for row in range(0, 9):
            for col in range(0, 9):
                if grid[row][col] != 0:
                    non_empty_squares.append((row, col))
        shuffle(non_empty_squares)
        return non_empty_squares

    def remove_numbers(self, empty_squares):
        non_empty_squares = self.get_non_empty_squares(self.board)
        non_empty_squares_count = len(non_empty_squares)
        rounds = 3
        while rounds > 0 and non_empty_squares_count > 81 - empty_squares:

            row, col = non_empty_squares.pop()
            non_empty_squares_count -= 1
            # Remember its cell value in case we need to put it back
            removed_square = self.board[row][col]
            self.board[row][col] = 0
            # Take a full copy of the grid
            grid_copy = copy.deepcopy(self.board)
            # Count the number of solutions that this grid has
            self.counter = 0
            self.solve_sudoku(grid_copy)
            # If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
            if self.counter != 1:
                self.board[row][col] = removed_square
                non_empty_squares_count += 1
                rounds -= 1
        return
