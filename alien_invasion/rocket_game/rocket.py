import pygame

class Rocket:
    """A class for managing rockets on the screen."""
    
    def __init__(self, rocket_game):
        """Creats a rocket object and sets ifs starting location."""
        self.screen = rocket_game.screen
        self.settings = rocket_game.settings
        self.screen_rect = rocket_game.screen.get_rect()

        # Load the rocket image and get its rect.
        self.image = pygame.image.load('images/Everly.bmp')
        self.rect = self.image.get_rect()

        # Start each new image at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store floats for the rocket's exact horizontal and vertical positions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag: start with a rocket that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        # Update the ship's x value, not the rect's.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draws the rocket on the screen at its current location."""
        self.screen.blit(self.image, self.rect)
