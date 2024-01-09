import pygame
import sys

class EmptyScreen:
    """A class to manage the overall game."""
    
    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption('Print Keys Game')
        self.bg_color = (255, 255, 255)


    def run_game(self):
        """start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responds to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                else:
                    print(event.key)

    def _update_screen(self):
        """Update image on the screen, and flip to the new screen."""
        self.screen.fill(self.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

def main():
    # Make a game instance, and run the game.
    empty_screen = EmptyScreen()
    empty_screen.run_game()

if __name__ == '__main__':
    main()