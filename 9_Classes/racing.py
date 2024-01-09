import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Car properties
car_width = 50
car_height = 80
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 10
car_speed = 5

# Enemy car properties
enemy_width = 50
enemy_height = 80
enemy_speed = 5
enemy_frequency = 25  # Increase this value for fewer enemies
enemy_x = 0
enemy_y = 0

# Fonts
font = pygame.font.Font(None, 36)

# Score
score = 0

def draw_car(x, y):
    pygame.draw.rect(screen, RED, [x, y, car_width, car_height])

def draw_enemy(x, y):
    pygame.draw.rect(screen, WHITE, [x, y, enemy_width, enemy_height])

def display_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width:
        car_x += car_speed

    # Move the enemy cars
    if random.randint(0, enemy_frequency) == 0:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y -= enemy_height
    else:
        enemy_y += enemy_speed

    # Collision detection
    if (
        car_x < enemy_x + enemy_width
        and car_x + car_width > enemy_x
        and car_y < enemy_y + enemy_height
        and car_y + car_height > enemy_y
    ):
        print("Game Over! Your score:", score)
        pygame.quit()
        sys.exit()

    # If enemy cars reach the bottom, reset their position
    if enemy_y > SCREEN_HEIGHT:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
        enemy_y -= enemy_height
        score += 1

    # Draw background
    screen.fill((0, 0, 0))

    # Draw cars and enemies
    draw_car(car_x, car_y)
    draw_enemy(enemy_x, enemy_y)

    # Display score
    display_score(score)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)
