
import pygame
import os
from pygame.sprite import spritecollide

# The Powerup class represents a power-up in pacman. This class is inherited by the other powerup classes.
class Powerup:
    def __init__(self, position):
        self.position = position
        self.image = None
        self.rect = None

    def handle_event(self, player, powerups):
        collided_powerups = spritecollide(player, powerups, False)
        for powerup in collided_powerups:
            self.apply_effect(player)
            powerups.remove(self)

    def apply_effect(self, player):
        pass