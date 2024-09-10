import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300
LINE_WIDTH = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Board
board = np.zeros((3, 3))

# Player
player = 1

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# Function to draw lines
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), LINE_WIDTH)

# Function to draw X and O
def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, (col * 100 + 15, row * 100 + 15), (col * 100 + 85, row * 100 + 85), LINE_WIDTH)
                pygame.draw.line(screen, RED, (col * 100 + 85, row * 100 + 15), (col * 100 + 15, row * 100 + 85), LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLUE, (col * 100 + 50, row * 100 + 50), 38, LINE_WIDTH)

# Function to check for a win
def check_win(player):
    for row in range(3):
        if np.all(board[row, :] == player):
            return True
    for col in range(3):
        if np.all(board[:, col] == player):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == player:
        return True
    if board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    return False

# Function to restart the game
def restart():
    
    board = np.zeros((3, 3))
    player = 1
    screen.fill(WHITE)
    draw_lines()

# Main game loop
screen.fill(WHITE)
draw_lines()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not np.all(board):
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked_row = mouse_y // 100
            clicked_col = mouse_x // 100

            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if check_win(player):
                    print(f"Player {player} wins!")
                    restart()
                player = 3 - player

            draw_figures()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
