import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define shapes
SHAPE_I = [[[1, 1, 1, 1]],
           [[1], [1], [1], [1]]]

SHAPE_O = [[[1, 1],
            [1, 1]]]

SHAPE_T = [[[0, 1, 0],
            [1, 1, 1]],
           [[1, 0],
            [1, 1],
            [1, 0]],
           [[1, 1, 1],
            [0, 1, 0]],
           [[0, 1],
            [1, 1],
            [0, 1]]]

SHAPE_J = [[[1, 0, 0],
            [1, 1, 1]],
           [[1, 1],
            [1, 0],
            [1, 0]],
           [[1, 1, 1],
            [0, 0, 1]],
           [[0, 1],
            [0, 1],
            [1, 1]]]

SHAPE_L = [[[0, 0, 1],
            [1, 1, 1]],
           [[1, 0],
            [1, 0],
            [1, 1]],
           [[1, 1, 1],
            [1, 0, 0]],
           [[1, 1],
            [0, 1],
            [0, 1]]]

SHAPE_S = [[[0, 1, 1],
            [1, 1, 0]],
           [[1, 0],
            [1, 1],
            [0, 1]]]

SHAPE_Z = [[[1, 1, 0],
            [0, 1, 1]],
           [[0, 1],
            [1, 1],
            [1, 0]]]

SHAPES = [SHAPE_I, SHAPE_O, SHAPE_T, SHAPE_J, SHAPE_L, SHAPE_S, SHAPE_Z]

# Define constants
BLOCK_SIZE = 20
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
SCORE_WIDTH = 100
FONT_SIZE = 24

# Initialize Pygame
pygame.init()

# Set up fonts
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH + SCORE_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Set up clock
clock = pygame.time.Clock()

def create_block():
    """
    Randomly creates a block from the available shapes
    """
    return random.choice(SHAPES)

def rotate_shape(shape, direction):
    """
    Rotates a shape either clockwise or counterclockwise
    """
    if direction == "cw":
        return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0])-1, -1, -1)]
    elif direction == "ccw":
        return [[shape[y][x] for y in range(len(shape)-1, -1, -1)] for x in range(len(shape[0]))]

def draw_block(x, y, shape, color):
    """
    Draws a block on the screen
    """
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                pygame.draw.rect(screen, color, (x + j * BLOCK_SIZE, y + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def check_collision(x, y, shape, grid):
    """
    Checks if a block collides with the existing grid or the boundaries of the screen
    """
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                if (x + j < 0 or x + j >= SCREEN_WIDTH / BLOCK_SIZE or
                        y + i >= SCREEN_HEIGHT / BLOCK_SIZE or grid[y // BLOCK_SIZE + i][x // BLOCK_SIZE + j]):
                    return True
    return False

def update_score(score):
    """
    Updates the score on the screen
    """
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH + 10, 10))

def draw_grid(grid):
    """
    Draws the existing blocks on the grid
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                pygame.draw.rect(screen, WHITE, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def remove_row(grid, row):
    """
    Removes a row from the grid
    """
    del grid[row]
    grid.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
    return grid

def remove_completed_rows(grid):
    """
    Removes completed rows from the grid and updates the score
    """
    rows_cleared = 0
    for i in range(len(grid)):
        if all(grid[i]):
            grid = remove_row(grid, i)
            rows_cleared += 1
    return grid, rows_cleared

def main():
    """
    Main function for running the game
    """
    grid = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    current_block = create_block()
    next_block = create_block()
    block_x, block_y = SCREEN_WIDTH // 2, 0
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(block_x - BLOCK_SIZE, block_y, current_block[0], grid):
                        block_x -= BLOCK_SIZE
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(block_x + BLOCK_SIZE, block_y, current_block[0], grid):
                        block_x += BLOCK_SIZE
                elif event.key == pygame.K_UP:
                    current_block[0] = rotate_shape(current_block[0], "cw")
                    if check_collision(block_x, block_y, current_block[0], grid):
                        current_block[0] = rotate_shape(current_block[0], "ccw")
                elif event.key == pygame.K_DOWN:
                    if not check_collision(block_x, block_y + BLOCK_SIZE, current_block[0], grid):
                        block_y += BLOCK_SIZE

        # Move the block down
        if not check_collision(block_x, block_y + BLOCK_SIZE, current_block[0], grid):
            block_y += BLOCK_SIZE
        else:
            # Add the block to the grid






