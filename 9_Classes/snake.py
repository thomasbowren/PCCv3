import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 800
GRID_SIZE = 20
SNAKE_SIZE = GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initial snake position and direction
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (GRID_SIZE, 0)

# Initial food position
food = (WIDTH // 2, HEIGHT // 2)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Change snake direction based on arrow key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, GRID_SIZE):
        snake_direction = (0, -GRID_SIZE)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -GRID_SIZE):
        snake_direction = (0, GRID_SIZE)
    elif keys[pygame.K_LEFT] and snake_direction != (GRID_SIZE, 0):
        snake_direction = (-GRID_SIZE, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-GRID_SIZE, 0):
        snake_direction = (GRID_SIZE, 0)

    # Update snake position
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Check for collisions with walls
    if (
        new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # Check for collisions with itself
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    # Check for collisions with food
    if new_head == food:
        snake.append(snake[-1])  # Grow the snake
        food = (random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE, random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(10)  # You can adjust this value to change the snake's speed
