import pygame

pygame.init()

# Set up the display dimensions
width = 800  # You can change this to your desired window width
height = 600  # You can change this to your desired window height

# Set up the display
screen = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Game logic and drawing here
    
    pygame.display.flip()

pygame.quit()
