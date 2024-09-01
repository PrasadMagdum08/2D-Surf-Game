import pygame


# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 600


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Surf Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
