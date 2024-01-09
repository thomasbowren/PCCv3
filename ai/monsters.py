import sys
import pygame
from settings import Settings
from monster_hunter import MonsterHunter

class Monsters:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.monster_hunter = MonsterHunter(self)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.monster_hunter.blitme()    
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
def main():
    # Make a game instance, and run the game.
    monsters = Monsters()
    monsters.run_game()

if __name__ == '__main__':
    main()