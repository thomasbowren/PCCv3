import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Paddle properties
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Ball properties
BALL_SIZE = 20
BALL_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Paddle positions
left_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
right_paddle_y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2

# Ball position and velocity
ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
ball_dx = random.choice([1, -1]) * BALL_SPEED
ball_dy = random.uniform(-1, 1) * BALL_SPEED

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= SCREEN_HEIGHT - BALL_SIZE:
        ball_dy *= -1

    # Ball collision with paddles
    if (
        ball_x <= PADDLE_WIDTH
        and left_paddle_y <= ball_y <= left_paddle_y + PADDLE_HEIGHT
    ) or (
        ball_x + BALL_SIZE >= SCREEN_WIDTH - PADDLE_WIDTH
        and right_paddle_y <= ball_y <= right_paddle_y + PADDLE_HEIGHT
    ):
        ball_dx *= -1

    # Ball out of bounds (score)
    if ball_x < 0 or ball_x > SCREEN_WIDTH:
        ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        ball_dx = random.choice([1, -1]) * BALL_SPEED
        ball_dy = random.uniform(-1, 1) * BALL_SPEED

    # Draw background
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, [0, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT])
    pygame.draw.rect(
        screen,
        WHITE,
        [SCREEN_WIDTH - PADDLE_WIDTH, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT],
    )

    # Draw ball
    pygame.draw.rect(screen, WHITE, [ball_x, ball_y, BALL_SIZE, BALL_SIZE])

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
