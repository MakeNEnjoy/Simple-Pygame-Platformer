import pygame
from pygame.image import load 

display_width = 1920
display_height = 1080

black = (0, 0, 0)
white = (255, 255, 255)

floor_y = display_height * 0.8

player_model = load('player.png')
player_height = 150
player_width = 75

KEY_UP = pygame.K_w
KEY_RIGHT = pygame.K_d
KEY_LEFT = pygame.K_a
KEY_QUIT = pygame.K_ESCAPE

fall_speed = 0.25
jump_height = -15
jump_acc = 0.07
run_speed = 3

wall_model = load('wall.png')
wall_height = 350
wall_width = 75

floor_model = load('floor.png')
floor_height = 75
floor_width = 350

portal_model = load('portal.png')
portal_height = 150
portal_width = 75

long_floor_model = load('long_floor.png')
long_floor_width = 1845
long_floor_height = floor_height