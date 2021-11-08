import pygame


def solve(grid):
    grid.update_model()
    grid.restore_generated(grid.window)
    find = grid.find_empty()
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(grid.model, i, (row, col)):
            grid.model[row][col] = i
            grid.board[row][col].set_value(i)
            grid.board[row][col].draw_change(grid.window)
            grid.update_model()
            pygame.display.update()
            pygame.time.delay(100)

            if solve(grid):
                return True

            grid.model[row][col] = 0
            grid.board[row][col].set_value(0)
            grid.update_model()
            grid.board[row][col].draw_change(grid.window)
            pygame.display.update()
            pygame.time.delay(100)

    return False


def valid(model, num, pos):
    for i in range(len(model[0])):
        if model[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(model)):
        if model[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if model[i][j] == num and (i, j) != pos:
                return False

    return True
