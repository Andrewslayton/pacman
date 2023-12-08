import pygame 
from Player import Player

# The Scoreboard class represents the game's scoreboard.
class Scoreboard:
    # The constructor initializes the player's score and lives.
    def __init__(self, player):
        self.player = player
        self.player.score = 0  # Initialize the player's score to 0.
        self.player.lives = 5  # Initialize the player's lives to 5.

    # The update_score method increases the player's score by a certain number of points.
    def update_score(self, points):
        self.player.score += points  # Increase the player's score by the given number of points.

    # The display method displays the player's score, lives, and goal on the screen.
    def display(self, screen):
        font = pygame.font.SysFont(None, 36)  # Create a font object.
        # Render the player's score, lives, and goal as text objects.
        score_text = font.render(f'Score: {self.player.score}', True, (255, 255, 255))
        life_text = font.render(f'Lives: {self.player.lives}', True, (255, 255, 0))
        goal_text = font.render(f'Goal: 10000', True, (255, 255, 255))
        # Draw the text objects on the screen.
        screen.blit(score_text, (20, 20))
        screen.blit(goal_text, (20, 90))
        screen.blit(life_text, (0, 580))
