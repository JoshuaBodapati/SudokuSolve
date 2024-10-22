import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Font settings
FONT = pygame.font.SysFont("comicsans", 40)
SMALL_FONT = pygame.font.SysFont("comicsans", 20)

# Dimensions
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE

# Empty board
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
original_board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid(win):
    win.fill(WHITE)
    # Draw the grid lines
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            thickness = 4  # Thicker lines for 3x3 subgrids
        else:
            thickness = 1
        pygame.draw.line(win, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), thickness)
        pygame.draw.line(win, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), thickness)

def draw_numbers(win, board):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = board[row][col]
            if num != 0:
                # Differentiate between original and user-input numbers
                color = BLACK if original_board[row][col] != 0 else BLUE
                num_text = FONT.render(str(num), True, color)
                win.blit(num_text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 6))

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board, win):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        draw(win, board)
                        pygame.display.update()
                        time.sleep(0.05)

                        if solve_sudoku(board, win):
                            return True

                        board[row][col] = 0
                        draw(win, board)
                        pygame.display.update()
                        time.sleep(0.05)
                return False
    return True

def get_cell_pos(mouse_pos):
    x, y = mouse_pos
    return y // CELL_SIZE, x // CELL_SIZE

def draw(win, board):
    draw_grid(win)
    draw_numbers(win, board)
    pygame.display.update()

def randomize_board(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            board[i][j] = 0  # Reset the board before randomizing
    
    # Add random numbers to the board while respecting Sudoku rules
    attempts = 10
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        num = random.randint(1, 9)
        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
            original_board[row][col] = num
        attempts -= 1
    draw(WIN, board)


def main():
    selected = None
    run = True
    while run:
        draw(WIN, board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                selected = get_cell_pos(pos)
            if event.type == pygame.KEYDOWN:
                if selected and event.key in range(pygame.K_1, pygame.K_9+1):
                    num = event.key - pygame.K_0
                    row, col = selected
                    # Allow changing only if it's not an original number
                    if original_board[row][col] == 0:
                        board[row][col] = num
                if event.key == pygame.K_BACKSPACE and selected:
                    row, col = selected
                    # Clear the cell if it's not an original number
                    if original_board[row][col] == 0:
                        board[row][col] = 0
                if event.key == pygame.K_RETURN:  # Start solving when 'Enter' is pressed
                    solve_sudoku(board, WIN)
                if event.key == pygame.K_c:  # Reset board when 'C' is pressed
                    for r in range(GRID_SIZE):
                        for c in range(GRID_SIZE):
                            board[r][c] = original_board[r][c]
                    draw(WIN, board)
                if event.key == pygame.K_r:  # Randomize board when 'R' is pressed
                    randomize_board(board)
    pygame.quit()

main()
