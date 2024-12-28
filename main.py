import pygame
import random
import time as t
# Initialize pygame
pygame.init()

# Set up the game window
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define the game variables
block_size = 20
grid_width = 20
grid_height = 15

# Create the game grid
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

# Define the tetromino shapes
tetrominoes = [
    [[0, 0, 0], [1, 1, 1], [0, 1, 0]],  # I
    [[0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0]],  # O
    [[0, 0, 3], [0, 3, 3], [3, 3, 0]],  # J
    [[0, 4, 0], [4, 4, 4], [0, 0, 0]],  # L
    [[0, 5, 0], [5, 5, 5], [0, 0, 5]],  # S
    [[0, 6, 6], [6, 6, 0], [0, 0, 0]],  # Z
    [[0, 7, 7], [0, 7, 7]]  # T
]

# Define the game functions
def draw_grid():
    for i in range(grid_height):
        for j in range(grid_width):
            pygame.draw.rect(screen, WHITE, (j * block_size, i * block_size, block_size, block_size), 1)

def draw_tetromino(tetromino, x, y):
    for i in range(len(tetromino)):
        for j in range(len(tetromino[i])):
            if tetromino[i][j] != 0:
                pygame.draw.rect(screen, get_color(tetromino[i][j]), (x + j * block_size, y + i * block_size, block_size, block_size))

def get_color(color_code):
    if color_code == 1:
        return RED
    elif color_code == 2:
        return GREEN
    elif color_code == 3:
        return BLUE
    elif color_code == 4:
        return YELLOW
    elif color_code == 5:
        return (0, 255, 255)  # Cyan
    elif color_code == 6:
        return (255, 165, 0)  # Orange
    elif color_code == 7:
        return (128, 0, 128)  # Purple
    else:
        return BLACK

# Game loop
running = True
while running:
    color = random.randint(0, 255)
    t.sleep(3)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Draw the tetromino
    tetromino = random.choice(tetrominoes)
    x = 5
    y = 0
    draw_tetromino(tetromino, x * block_size, y * block_size)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()