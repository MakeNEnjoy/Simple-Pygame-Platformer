import pygame
from constants import *

pygame.init()

gameDisplay = pygame.display.set_mode(
    (display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Dash 2.0')
clock = pygame.time.Clock()
