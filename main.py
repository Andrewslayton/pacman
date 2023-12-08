import pygame
import os
from Player import Player
from Maze import Maze
from Ghost import Ghost
from Scoreboard import Scoreboard
from pygame.sprite import spritecollide
from Powerup import Powerup 
from Lifepowerup import LifePowerup
from speedpowerup import SpeedPowerup
from Invinciblepowerup import Invinciblepowerup


class rungame:
    # The constructor initializes the game.
    def __init__(self):
        pygame.init()  # Initialize all imported pygame modules.
        self.screen = pygame.display.set_mode((800, 600))  # Set the size of the window.
        self.clock = pygame.time.Clock()  # Create a clock object to control the frame rate.
        # Create a player object at position (100, 100) with the image 'pacman_.png'.
        self.player = Player((100, 100), os.path.join('assets', 'pacman_.png'))  
        self.playerT = pygame.sprite.GroupSingle(self.player)  
        self.maze = Maze()  
        # Define the positions of all 4 of the  ghosts.
        ghost_positions = [(0, 0), (0, 600), (800, 0), (800, 600)]   
        # Create a group of ghosts at the defined positions and assing them the png of ghost'.
        self.ghosts = pygame.sprite.Group(Ghost(pos, os.path.join('assets', 'ghost.png')) for pos in ghost_positions)
        self.scoreboard = Scoreboard(self.player)  
        self.is_running = True  
        self.level = 1  
        self.powerups = pygame.sprite.Group()  
        life_powerup = LifePowerup((100, 100))  # just to initalize the powerup
        speed_powerup = SpeedPowerup((200, 200))
        inv_powerup = Invinciblepowerup((300,400))  # just to initalize the powerup
        self.powerups.add(life_powerup)  # Add the life power-up to the group.
        self.powerups.add(speed_powerup)  # Add the speed power-up to the group.

    # The run_game_loop method runs the game loop.
    # This method handles events, updates the game state, and renders the game.
    def run_game_loop(self):
        while self.is_running:  
            self.events_t()
            self.handle_actions()
            self.render()
            self.clock.tick(60)  

    #The events_t method handles the events of keypressing and quitting the game.
    def events_t(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.player.handle_keypress(event.key)

    # The handle_actions method handles most of the events happening between player and game.
    def handle_actions(self):
        self.playerT.update(self.maze)
        for ghost in self.ghosts:
            self.ghosts.update()
            # if player is not invincible, ghosts chase player, if not ghosts run away from player
            if self.player._invincible == False:
                ghost.chase_player(self.player)
            else:
                ghost.run_away(self.player)
            # Check if the player has collided with a ghost and if the player is invincible or not.
            collide_ghosts = pygame.sprite.spritecollide(self.player, self.ghosts, False)
            for ghost in collide_ghosts:
                    if self.player._invincible == False:
                        self.reset()
                    else:
                        self.ghosts.remove(ghost)
                        self.scoreboard.update_score(100) 
        maze_x = self.player.position[0] // self.maze.wall_size
        maze_y = self.player.position[1] // self.maze.wall_size
        # Check if the player has eaten a power-up. If yes apply the power-up's effect and remove it from maze.
        for powerup in self.maze.power_ups:
            if spritecollide(self.player, [powerup], False):
                powerup.handle_event(self.player, self.maze.power_ups)
                self.maze.eaten_powerup(self.player, powerup)
        # Check if the player has eaten a dot. If so, increase the player's score and remove the dot from the maze.
        if self.maze.layout[maze_y][maze_x] == '1' :  
            self.player._direction = None
            print("ouch thats a wall") 
        if self.maze.layout[maze_y][maze_x] == '0':  
            print("YUMMY!")
            self.player.eat_dot()
            self.maze.eaten_dot((maze_x, maze_y))
        if self.player.lives == 0:
            self.is_running = False
            print("lost!!!!!!!")
        if self.player.score >= 10000:
            print ("You win!!!")
            self.next_level()

    # The render method is responsibl for screen display.
    def render(self):
        self.screen.fill((0, 0, 0))  
        self.maze.draw(self.screen)
        self.playerT.draw(self.screen)
        self.ghosts.draw(self.screen)
        self.scoreboard.display(self.screen)
        pygame.display.flip()

    # The reset method resets the game state in the event of a pacmans death.
    # This method does not entirely reset the game.
    def reset(self):
        self.player.reset()  
        ghost_positions = [(0, 0), (0, 600), (800, 0), (800, 600)]   
        self.ghosts = pygame.sprite.Group(Ghost(pos, os.path.join('assets', 'ghost.png')  ) for pos, in zip(ghost_positions))
        self.maze.reset()  
        self.player.lose_life() 
        self.player._invincible = False
        if self.player.lives == 0:
            self.is_running = False
    # Next level method is responsible for the transition between levels.
    def next_level(self):
        self.reset()
        self.player.gain_life()
        self.player.score = 0
        self.maze.next_level()
        if self.level==4:
            self.is_running = False
            print("You win!")
        

def main():
    game = rungame()
    game.run_game_loop()
    pygame.quit()

if __name__ == "__main__":
    main()
