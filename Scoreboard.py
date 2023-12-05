import pygame 
from Player import Player
class Scoreboard:
    def __init__(self, player):
        self.player = player
        self.player.score = 0
        self.player.lives = 5

    def update_score(self, points):
        self.score += points

    def display(self, screen):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {self.player.score}', True, (255, 255, 255))
        life_text = font.render(f'Lives: {self.player.lives}', True, (255, 255, 0))
        goal_text = font.render(f'Goal: 10000', True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        screen.blit(goal_text, (20, 90))
        screen.blit(life_text, (0, 580))
