import pygame
import os
from Player import Player
from Maze import Maze
from Ghost import Ghost
from Scoreboard import Scoreboard
from pygame.sprite import spritecollide
from Powerup import Powerup 

class GameRun:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  
        self.clock = pygame.time.Clock()  
        self.player = Player((100, 100), os.path.join('assets', 'pacman_.png'))  
        self.playerT = pygame.sprite.GroupSingle(self.player)
        self.maze = Maze() 
        ghost_positions = [(0, 0), (0, 600), (800, 0), (800, 600)]   
        self.ghosts = pygame.sprite.Group(Ghost(pos, os.path.join('assets', 'ghost.png')  ) for pos, in zip(ghost_positions))
        self.scoreboard = Scoreboard(self.player)
        self.is_running = True
        self.level = 1


    def run_game_loop(self):
        while self.is_running:
            self.handle_events()
            self.update_game_state()
            self.render()
            self.clock.tick(60)  

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                self.player.handle_keypress(event.key)

    def update_game_state(self):
        self.playerT.update()
        for ghost in self.ghosts:
            self.ghosts.update()
            ghost.chase_player(self.player.position)
            if spritecollide(self.player, self.ghosts, False):
                self.reset()
        maze_x = self.player.position[0] // self.maze.wall_size
        maze_y = self.player.position[1] // self.maze.wall_size
        self.Powerup.handle_event(self.player, self.maze, maze_x, maze_y)
        if self.maze.layout[maze_y][maze_x] == '1' :  
            self.player._direction = None
            print("ouch thats a wall")
        if self.maze.layout[maze_y][maze_x] == '0':  
            print("YUMMY!")
            self.player.eat_dot()
            self.maze.eaten_dot((maze_x, maze_y))
        if self.maze.layout[maze_y][maze_x] == 's':
            self.Powerup.increase_speed()
            self.maze.eaten_dot((maze_x, maze_y))
        if self.maze.layout[maze_y][maze_x] == 'l':
            self.player.gain_life()
            self.maze.eaten_dot((maze_x, maze_y))
        if self.player.lives == 0:
            self.is_running = False
            print("lost!!!!!!!")
        if self.player.score >= 10000:
            print ("You win!")
            self.next_level()

    def render(self):
        self.screen.fill((0, 0, 0))  
        self.maze.draw(self.screen)
        self.playerT.draw(self.screen)
        self.ghosts.draw(self.screen)
        self.scoreboard.display(self.screen)
        pygame.display.flip()

    #not named well
    def reset(self):
        self.player.reset()  # Reset pacmans state
        ghost_positions = [(0, 0), (0, 600), (800, 0), (800, 600)]   
        self.ghosts = pygame.sprite.Group(Ghost(pos, os.path.join('assets', 'ghost.png')  ) for pos, in zip(ghost_positions))
        self.maze.reset()  # Reset the maze's state
        self.player.lives -= 1  # Decrease pacmans lives
        if self.player.lives == 0:
            self.is_running = False

    def next_level(self):
        self.reset()
        self.player.score = 0
        self.maze.next_level()
        self.level+=1
        if self.level==4:
            self.is_running = False
            print("You win!")
        


def main():
    game = GameRun()
    game.run_game_loop()
    pygame.quit()

if __name__ == "__main__":
    main()

