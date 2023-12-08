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
        self._invincible = False

    @property
    def position(self):
        return self.rect.topleft 
    
    # The reset method resets the player's position and speed to their original values.
    def reset(self):
        self.rect.center = (100, 100)
        self._speed = 6 

    @position.setter
    def position(self, value):
        self.rect.topleft = value

    #use of pythons property operators to make the score a property instead of get set 
    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        self._lives = value
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    #the handle_keypress method changes the player's direction based on the key pressed
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

    # the update method updates the player's position based on its current direction.
    # Update verifies if player is not moving into a wall
    def update(self, maze):
        x,y = self.position
        if self._direction == 'UP' and not maze.wall((x, y - self._speed)):
            self.position = (x, y - self._speed)
        elif self._direction == 'DOWN' and not maze.wall((x, y + self._speed + 10)):
            self.position = (x, y + self._speed)
        elif self._direction == 'LEFT'  and not maze.wall((x - self._speed , y)):
            self.position = (x - self._speed, y)
        elif self._direction == 'RIGHT' and not maze.wall((x + self._speed + 10 , y)):
            self.position = (x + self._speed, y)
        pass

   
    def gain_life(self):
        self.lives += 1
    
    def lose_life(self):
        self.lives -= 1

    def increase_speed(self):
        self._speed += 2  

    def eat_dot(self):
        self.score += 110  
        print(self.score)
        
    def become_invincible(self):
        self._invincible = True

        


