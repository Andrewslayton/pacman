import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (22, 22))
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self._current_direction = 'UP'
    
    @property
    def position(self):
        return self.rect.topleft

    def reset(self): 
        self.rect.center = (400, 300)  

    # Update give the ghost a new position based on its current direction
    def update(self):
        x, y = self.rect.topleft
        if self._current_direction == 'UP':
            y -= 1
        elif self._current_direction == 'DOWN':
            y += 1
        elif self._current_direction == 'LEFT':
            x -= 1
        elif self._current_direction == 'RIGHT':
            x += 1
        self.rect.topleft = (x, y)

    # Chase_player method is a very simple AI(not really) that makes the ghost chase the player to its exact position.
    def chase_player(self, player):
        x, y = player.position
        gx, gy = self.rect.topleft
        if abs(x - gx) > abs(y - gy):
            self._current_direction = 'LEFT' if x < gx else 'RIGHT'
        else:
            self._current_direction = 'UP' if y < gy else 'DOWN'
    def run_away (self, player):
        x, y = player.position
        gx, gy = self.rect.topleft
        if abs(x - gx) > abs(y - gy):
            self._current_direction = 'RIGHT' if x < gx else 'LEFT'
        else:
            self._current_direction = 'DOWN' if y < gy else 'UP'