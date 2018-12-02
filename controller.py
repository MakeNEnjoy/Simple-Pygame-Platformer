import pygame
from constants import *

def controller(level, events):
	for event in events:
		if(event.type == pygame.QUIT):
			level.exit_game = True

		if(event.type == pygame.KEYDOWN):
			if(event.key == KEY_LEFT):
				level.sprites[0].move(0)
			elif(event.key == KEY_RIGHT):
				level.sprites[0].move(2)
			elif(event.key == KEY_UP):
				level.sprites[0].move(1)
			elif(event.key == KEY_QUIT):
				level.exit_game = True
		if(event.type == pygame.KEYUP):
			if(event.key == KEY_LEFT):
				level.sprites[0].move(3)
			elif(event.key == KEY_RIGHT):
				level.sprites[0].move(4)
			elif(event.key == KEY_UP):
				level.sprites[0].move(5)
			
