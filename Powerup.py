import  pygame
import os 
class Powerup:
    def __init__(self,type,position):
        self.type = type
        self.position = position
        if type == 'life':
            self.image = pygame.image.load(os.path.join('assets', 'life_power.png'))
            self.image = pygame.transform.scale(self.image, (18, 18))

        elif type == 'speed':
            self.image = pygame.image.load(os.path.join('assets', 'orange.png'))
            self.image = pygame.transform.scale(self.image, (18, 18))

    def handle_event(self, player, maze):
        player_x, player_y = player.position
        powerup_x, powerup_y = self.position
        if player_x == powerup_x and player_y == powerup_y:
            if self.type == 'life':
                player.gain_life()
            elif self.type == 'speed':
                player.increase_speed()
            maze.eaten_dot((powerup_x, powerup_y))