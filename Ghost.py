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

    def chase_player(self, player_pos):
        px, py = player_pos
        gx, gy = self.rect.topleft
        if abs(px - gx) > abs(py - gy):
            self._current_direction = 'LEFT' if px < gx else 'RIGHT'
        else:
            self._current_direction = 'UP' if py < gy else 'DOWN'
