import pygame
from constants import *
from intilialize import *
from classes import player
from levels import *
from controller import controller
import physics

user = player()

level = level1(user)

while not level.exit_game:
	
	controller(level, pygame.event.get())

	physics.tick(level)

	gameDisplay.fill(white)
	for sprite in level.sprites:
		sprite.update_position()
	pygame.display.update()
	clock.tick()

pygame.quit()
quit()
