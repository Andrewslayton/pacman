import pygame
from Powerup import Powerup
import os
from pygame.sprite import Sprite

# The SpeedPowerup class represents a speed power-up in the game. This class inherits from the Powerup class.
# Inheriting from the Powerup class is necessary because the SpeedPowerup class needs to have the same methods as the Powerup class.
class SpeedPowerup(Powerup, pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        Powerup.__init__(self, position)
        super().__init__(position)
        self.image = pygame.image.load(os.path.join('assets', 'orange.png'))
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect(topleft=self.position)

    def apply_effect(self, player):
        player.increase_speed()