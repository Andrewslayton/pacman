import os 
import pygame
from pygame.sprite import Sprite
from Powerup import Powerup

# The InvinciblePowerup class represents an invincible power-up, this class inherits from the Powerup class.
class Invinciblepowerup(Powerup, pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        Powerup.__init__(self, position)
        super().__init__(position)
        self.image = pygame.image.load(os.path.join('assets', 'inv.png'))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(topleft=self.position)
    
    def apply_effect(self, player):
        player.become_invincible()
