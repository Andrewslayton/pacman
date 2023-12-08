import pygame
from Powerup import Powerup
from Lifepowerup import LifePowerup
from speedpowerup import SpeedPowerup
from Invinciblepowerup import Invinciblepowerup
import pygame.sprite
class Maze():
    # constructor that initializes the maze
    #initialize the colors,sizes, dot to white, blank to black, power ups and the layout
    def __init__(self):
        self.wall_color = (0, 0, 255)  
        self.dot_color = (255, 255, 255)  
        self.blank_color = (0, 0, 0)  
        self.wall_size = 20
        self.dot_size = 5
        self.level = 1
        self.power_ups = pygame.sprite.Group()
        self.layout = self.load_layout()

    # This is how i made the layout of the maze 1 is a wall 0 is a dot l and s are power ups
    def load_layout(self):
        return [
            "111111111111111111111111111111111111111",
            "100000000000000000000000000000000000001",
            "100000000000000000000000000000000000001",
            "10s000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "1000000000000000111111110000001000s0001",
            "100000000000000000010000000000100000001",
            "100000000000000000010000000000100000001",
            "111111110000000000010000000000100000001",
            "100l000100000000000100000000001000l0001",
            "100000000000000000010000000000100s00001",
            "1000000000000000l0000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "1000000000000000s0000000000000100000001",
            "100000000000000000000000M00000100000001",
            "100001110000000000000000000000100000001",
            "100000110000000000000000000000100000001",
            "100000110000000000000000000000100000001",
            "100000110000000000000000000000100000001",
            "100l001100000000000000000010001000l0001",
            "100000000000000000000000000001100000001",
            "100000000000000000000000000000100000001",            
            "111111111111111111111111111111111111111", 
        ]


    def load_layout_2(self):
         return [
            "111111111111111111111111111111111111111",
            "100000000000000000000000000000000000001",
            "100000000000000000000000000000000000001",
            "10s000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000010000000000000000000000100000001",
            "100000010000000000000000000000100000001",
            "100000010000000000000000000000100000001",
            "000000010000000000000000000000100000001",
            "0000000100000000111111110000001000s0001",
            "000000010000000000010000000000100000001",
            "000000010000000000010000000000111111001",
            "111111110000000000010000000000100000001",
            "100l000100000000000100000000001000l0001",
            "100000000000000000010000000000100s00001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "1000000000000000s0000000000000100000001",
            "100000000000000000000000000000100000001",
            "111111110000000000000000000000100000001",
            "100000110000000000000000000000100000001",
            "100000111111111110000000000000100000001",
            "100000110000000000000000000000100000001",
            "100l001100000000000000000010001000l0001",
            "100000000000000000000000000001100000001",
            "100000000000000000000000000000100000001",            
            "111111111111111111111111111111111111111", 
        ]
    def load_layout_3(self):
         return [
            "111111111111111111111111111111111111111",
            "100000000000000000000000000000000000001",
            "100000000000000000000000000000000000001",
            "10s000000000000000100000000000100000001",
            "100000000000000000100000000000100000001",
            "100000010000000000100000000000100000001",
            "100000010000000000100000000000100000001",
            "100000010000000000100000000000100000001",
            "000000010000000000100000000000100000001",
            "0000000100000000111111110000001000s0001",
            "000000010000000000010000000000100000001",
            "000000010000000000010000000000111111001",
            "111111110000000000010000000000100000001",
            "100l000100000000000100000000001000l0001",
            "100000000000000000010000000000100s00001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "100000000000000000000000000000100000001",
            "1001111000000000s0000000000000100000001",
            "1000l0100000000000000000000000100000001",
            "111000110000000000000010000000100000001",
            "100000110000000000000010000000100000001",
            "100000111111111110000010000000100000001",
            "100000110000000000000010000000100000001",
            "100l001100000000000000100010001000l0001",
            "100000000000000000000010000001100000001",
            "100000000000000000000010000000100000001",            
            "111111111111111111111111111111111111111", 
        ]
    
    # This is how i determine the layout of the maze in a reset
    def reset(self):
        if self.level==1:
            self.layout = self.load_layout()
        elif self.level==2:
            self.layout = self.load_layout_2()
        elif self.level==3:
            self.layout = self.load_layout_3()    

    # This is how i determine the layout of the maze in a next level, somewhat redundant.
    def next_level(self):
        self.level+=1
        if self.level==2:
            self.layout = self.load_layout_2()
        elif self.level==3:
            self.layout = self.load_layout_3()

    # This is how i update the layout of the maze. I have this method because its called multiple times.
    def update_maze_layout(self, grid_x, grid_y, value):
        row = list(self.layout[grid_y])
        row[grid_x] = value
        self.layout[grid_y] = ''.join(row)
    
    # Eaten_dot is called when the player eats a dot. It updates the layout of the maze.
    def eaten_dot(self, position,):
        x, y = position
        if self.layout[y][x] != "1":  # Check if it's not a wall
            self.update_maze_layout(x, y, "2")
            
    # Eaten_powerup is called when the player eats a powerup. It updates the layout of the maze.
    # Tis method had to be handled differently because powerups are sprites.
    # I had to remove the powerup itself intstead of the position of the dot in the layout.
    # This was because of the sprite size coliding with the player sometimes while not being in its exact location
    def eaten_powerup(self, player, powerup):
        if powerup in self.power_ups:
            self.power_ups.remove(powerup)
        x = powerup.rect.x // self.wall_size
        y = powerup.rect.y // self.wall_size
        row = list(self.layout[y])
        row[x] = '2'
        self.layout[y] = ''.join(row)

    def wall(self, position):
        x, y = position
        x //= self.wall_size  # Convert the x-coordinate to a column index.
        y //= self.wall_size  # Convert the y-coordinate to a row index.
        return self.layout[y][x] == '1'  

    # Draw method puts the layout on the screen. This converts the layout into a visual representation.
    # It also adds the powerups to the powerup group.
    # 1=wall, 0=dot, 2=blank, l=life powerup, s=speed powerup
    def draw(self, screen):
        self.power_ups = []
        for y, row in enumerate(self.layout):
            for x, cell in enumerate(row):
                pos_x, pos_y = x * self.wall_size, y * self.wall_size
                if cell == "1":
                    pygame.draw.rect(screen, self.wall_color, (pos_x, pos_y, self.wall_size, self.wall_size))
                elif cell == "0":
                    pygame.draw.circle(screen, self.dot_color, (pos_x + self.wall_size // 2, pos_y + self.wall_size // 2), self.dot_size)
                elif cell == "2":
                    pygame.draw.circle(screen, self.blank_color, (pos_x + self.wall_size // 2, pos_y + self.wall_size // 2), self.dot_size)
                elif cell == "l":
                    life_powerup = LifePowerup( (pos_x, pos_y))
                    self.power_ups.append(life_powerup)
                    screen.blit(life_powerup.image, (pos_x, pos_y))
                elif cell == "s":
                    speed_powerup = SpeedPowerup( (pos_x, pos_y))
                    self.power_ups.append(speed_powerup)
                    screen.blit(speed_powerup.image, (pos_x, pos_y))
                elif cell == "M":
                    inv_powerup = Invinciblepowerup((pos_x, pos_y))
                    self.power_ups.append(inv_powerup)
                    screen.blit(inv_powerup.image, (pos_x, pos_y))

                # elif cell == 'l':
                #     self.power_ups.append(Powerup('life', (x * self.wall_size, y * self.wall_size)))
                # elif cell == 's':
                #     self.power_ups.append(Powerup('speed', (x * self.wall_size, y * self.wall_size)))