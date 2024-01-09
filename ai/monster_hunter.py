import pygame

class MonsterHunter:
    """A class to manage monster hunters."""
    
    def __init__(self, ai_game):
        """Initializes a monster hunter and sets its target position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the monster hunter sprite and get its rect.
        self.image = pygame.image.load('images/monster_hunter.bmp')
        self.rect = self.image.get_rect()

        # Start each new monster at the bottom of the center screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the monster hunter at its current location."""
        self.screen.blit(self.image, self.rect)