# Importing Pygame
import pygame

# Initializate pygame
pygame.init()

# window size
screen_width = 800
screen_height = 600

# size variable

size = (screen_width, screen_height)

# Title
pygame.display.set_caption("Space Invaders by Leonardo Gonzalez")

# icon
icon = pygame.image.load("Sprites\Sprites\ship_4.png")
pygame.display.set_icon(icon)
# display_screen
screen = pygame.display.set_mode(size)

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False