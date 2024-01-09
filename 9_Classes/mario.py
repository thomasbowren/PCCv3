import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255,255)
BLACK = (0, 0, 0)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mario")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Mario properties
mario_x = 50
mario_y = SCREEN_HEIGHT - 100
mario_width = 50
mario_height = 50
mario_speed = 5
is_jumping = False
jump_count = 10

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and mario_x > 0:
        mario_x -= mario_speed
    if keys[pygame.K_RIGHT] and mario_x < SCREEN_WIDTH - mario_width:
        mario_x += mario_speed

    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            mario_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Draw background
    screen.fill(BLACK)

    # Draw Mario
    pygame.draw.rect(screen, WHITE, [mario_x, mario_y, mario_width, mario_height])

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
