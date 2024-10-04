import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FONT_COLOR = BLACK
FLIP_DUR = 0.3  # Flip duration in seconds
MATCH_FLIP_DUR = 0.3
TOP_BOTTOM_PADDING = 50  # Adjustable padding on top and bottom

# Adjustable parameters
N = 40  # Number of rows
M = 40  # Number of columns
FONT_SIZE = 120

# Load images
heads_img = pygame.image.load('heads.png')
tails_img = pygame.image.load('tails.png')

# Scale images to be the same size (adjust as needed)
penny_size = min(SCREEN_WIDTH // (M + 2), (SCREEN_HEIGHT - 2 * TOP_BOTTOM_PADDING) // N)  # Add 2 columns for text on sides
heads_img = pygame.transform.scale(heads_img, (penny_size, penny_size))
tails_img = pygame.transform.scale(tails_img, (penny_size, penny_size))

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Penny Grid")

# Font setup
font = pygame.font.SysFont(None, FONT_SIZE)

# To store penny flips
penny_grid = [[random.choice([True, False]) for _ in range(M)] for _ in range(N)]
last_flip_time = time.time()


def draw_grid(screen, N, M, penny_size):
    num_heads = 0
    num_tails = 0
    grid_left = (SCREEN_WIDTH - M * penny_size) // 2  # Center grid horizontally
    grid_top = (SCREEN_HEIGHT - N * penny_size) // 2  # Center grid vertically, accounting for padding
    
    # Draw grid of pennies
    for row in range(N):
        for col in range(M):
            x = grid_left + col * penny_size
            y = grid_top + row * penny_size
            is_heads = penny_grid[row][col]
            if is_heads:
                screen.blit(heads_img, (x, y))
                num_heads += 1
            else:
                screen.blit(tails_img, (x, y))
                num_tails += 1

    return num_heads, num_tails

def draw_text(screen, text, x, y, color, alignment='center'):
    """Draw text at (x, y), with an option for center alignment."""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if alignment == 'center':
        text_rect.center = (x, y)
    
    screen.blit(text_surface, text_rect)

def flip_pennies():
    global penny_grid
    penny_grid = [[random.choice([True, False]) for _ in range(M)] for _ in range(N)]

def main():
    global last_flip_time

    # Main loop
    running = True
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # Draw the penny grid and get counts
        num_heads, num_tails = draw_grid(screen, N, M, penny_size)

        # Check if it's time to flip the pennies
        current_time = time.time()
        if current_time - last_flip_time >= (MATCH_FLIP_DUR if num_heads == num_tails else FLIP_DUR):
            flip_pennies()
            last_flip_time = current_time


        # Change text color to blue if num_heads == num_tails, otherwise black
        text_color = BLUE if num_heads == num_tails else FONT_COLOR

        # Draw the number of heads on the left side
        draw_text(screen, f"{num_heads}", SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2 - FONT_SIZE // 2, text_color)
        draw_text(screen, "heads", SCREEN_WIDTH // 8, SCREEN_HEIGHT // 2 + FONT_SIZE // 2, text_color)

        # Draw the number of tails on the right side
        draw_text(screen, f"{num_tails}", SCREEN_WIDTH * 7 // 8, SCREEN_HEIGHT // 2 - FONT_SIZE // 2, text_color)
        draw_text(screen, "tails", SCREEN_WIDTH * 7 // 8, SCREEN_HEIGHT // 2 + FONT_SIZE // 2, text_color)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
