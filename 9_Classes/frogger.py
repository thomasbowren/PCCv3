import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FROG_SIZE = 50
CAR_WIDTH = 50
CAR_HEIGHT = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Frog properties
frog_x = SCREEN_WIDTH // 2 - FROG_SIZE // 2
frog_y = SCREEN_HEIGHT - FROG_SIZE - 10

# Car properties
car_speed = 5
cars = []

def draw_frog(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, FROG_SIZE, FROG_SIZE])

def draw_car(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, CAR_WIDTH, CAR_HEIGHT])

def game_over():
    font = pygame.font.SysFont(None, 55)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and frog_x > 0:
        frog_x -= 5
    if keys[pygame.K_RIGHT] and frog_x < SCREEN_WIDTH - FROG_SIZE:
        frog_x += 5
    if keys[pygame.K_UP] and frog_y > 0:
        frog_y -= 5
    if keys[pygame.K_DOWN] and frog_y < SCREEN_HEIGHT - FROG_SIZE:
        frog_y += 5

    # Move cars
    for car in cars:
        car[1] += car_speed
        if car[1] > SCREEN_HEIGHT:
            car[1] = 0 - CAR_HEIGHT
            car[0] = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)

        # Check for collision with frog
        if (
            frog_x < car[0] + CAR_WIDTH
            and frog_x + FROG_SIZE > car[0]
            and frog_y < car[1] + CAR_HEIGHT
            and frog_y + FROG_SIZE > car[1]
        ):
            game_over()

    # Create new cars at random intervals
    if random.randint(0, 100) < 5:
        car_x = random.randint(0, SCREEN_WIDTH - CAR_WIDTH)
        cars.append([car_x, 0 - CAR_HEIGHT])

    # Draw background
    screen.fill(BLACK)

    # Draw frog
    draw_frog(frog_x, frog_y)

    # Draw cars
    for car in cars:
        draw_car(car[0], car[1])

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
