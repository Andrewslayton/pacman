import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.original_I = pygame.transform.scale(self.image, (18, 18))
        self.image = self.original_I
        self.rect = self.image.get_rect()
        self.rect.topleft = (100,100)
        self._color = (255, 255, 0)  
        self._speed = 6
        self._direction = None
        self._lives = 5
        self._score = 0

    @property
    def position(self):
        return self.rect.topleft 
    
    def reset(self):
        # Reset the player's state
        self.rect.center = (100, 100)  # Reset the player's position to the center of the screen
        self._speed = 6  # Reset the player's speed to the initial speed
    
    @position.setter
    def position(self, value):
        self.rect.topleft = value

    def handle_keypress(self, key):
        if key == pygame.K_UP:
            self._direction = 'UP'
            self.image = pygame.transform.rotate(self.original_I, 90)
        elif key == pygame.K_DOWN:
            self._direction = 'DOWN'
            self.image= pygame.transform.rotate(self.original_I, 270)
        elif key == pygame.K_LEFT:
            self._direction = 'LEFT'
            self.image= pygame.transform.flip(self.original_I, True, False)
        elif key == pygame.K_RIGHT:
            self._direction = 'RIGHT'
            self.image= pygame.transform.rotate(self.original_I, 0)

    def update(self):
        if self._direction == 'UP':
            self.position = (self.position[0], self.position[1] - self._speed)
        elif self._direction == 'DOWN':
            self.position = (self.position[0], self.position[1] + self._speed)
        elif self._direction == 'LEFT':
            self.position = (self.position[0] - self._speed, self.position[1])
        elif self._direction == 'RIGHT':
            self.position = (self.position[0] + self._speed, self.position[1])
        pass

   
    def gain_life(self):
        self.lives += 1

    def increase_speed(self):
        self._speed += 2  

    def eat_dot(self):
        self.score += 110  
        print(self.score)
    


