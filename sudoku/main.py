import SudokuSolver
from SudokuGenerator import SudokuGenerator
from Grid import Grid, check_solution, victory, fail, redraw_window, update_time
import time

from SudokuSolver import *


def main():
    font = pygame.font.SysFont("comicsans", 20)
    window = pygame.display.set_mode((540, 620))
    pygame.display.set_caption("Sudoku")
    board = SudokuGenerator(10).board
    grid = Grid(board, 9, 9, 540, 540, window, 300)
    key = None
    start = time.time()
    status = 1
    is_resolved = False

    solve_button_height = 30
    solve_button_width = 75
    solve_button_x = 460
    solve_button_y = 585

    while True:
        play_time = round(grid.timer - time.time() + start)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    grid.clear()
                    key = None

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_RETURN:
                    i, j = grid.selected
                    if grid.board[i][j].temp != 0:
                        grid.place(grid.board[i][j].temp)

                    if grid.is_finished():
                        redraw_window(window, grid)
                        status = 0
                        if check_solution(grid):
                            victory(window)
                            is_resolved = True
                        else:
                            fail(window)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if is_resolved == False and solve_button_x <= pos[0] <= solve_button_x + solve_button_width and solve_button_y <= \
                        pos[1] <= solve_button_y + solve_button_height:
                    grid.restore_fields(window)
                    redraw_window(window, grid)
                    SudokuSolver.solve(grid)
                    status = 0
                    is_resolved = True
                clicked = grid.click(pos)
                if clicked:
                    grid.select(clicked[0], clicked[1])
                    key = None

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if status == 1:
            if grid.selected and key is not None:
                grid.set_temp(key)
            if play_time <= 0:
                redraw_window(window, grid)
                status = 0
                fail(window)

        if status == 1:
            redraw_window(window, grid)
            update_time(window, grid, play_time)

        pos = pygame.mouse.get_pos()

        if solve_button_x <= pos[0] <= solve_button_x + solve_button_width and solve_button_y <= pos[
            1] <= solve_button_y + solve_button_height:
            pygame.draw.rect(window, (230, 230, 230),
                             [solve_button_x, solve_button_y, solve_button_width, solve_button_height])
        else:
            pygame.draw.rect(window, (215, 215, 215),
                             [solve_button_x, solve_button_y, solve_button_width, solve_button_height])

        window.blit(font.render("Solve", 1, (137, 137, 137)), (solve_button_x, solve_button_y))

        pygame.display.update()


if __name__ == '__main__':
    main()
