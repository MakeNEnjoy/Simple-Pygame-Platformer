import pygame
from intilialize import *

class sprite:
	def __init__(self, picture, height, width):
		self.height = height
		self.width = width
		self.img = picture
		self.x = 0
		self.y = 0
	def update_position(self):
		gameDisplay.blit(self.img, (self.x, self.y))
	def getRect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)

class player(sprite):
	def __init__(self):

		sprite.__init__(self, player_model, player_height, player_width)

		self.vel_left = 0
		self.vel_right = 0
		self.vel_y = 0
		self.jumping = False
		self.left = False
		self.right = False
		self.level_go_pos = 1
		self.level_pos = 1

	def move(self, direction):
		if(direction == 0):
			self.left = True
		elif(direction == 1):
			self.jumping = True
		elif(direction == 2):
			self.right = True
		elif(direction == 3):
			self.left = False
		elif(direction == 4):
			self.right = False
		elif(direction == 5):
			self.jumping = False

class blockade(sprite):
	def __init__(self, model, height, width, pos):
		sprite.__init__(self, model, height, width)
		self.x, self.y = pos


class wall(blockade):
	def __init__(self, pos):
		blockade.__init__(self, wall_model, wall_height, wall_width, pos)

class floor(blockade):
	def __init__(self, pos):
		blockade.__init__(self, floor_model, floor_height, floor_width, pos)

class long_floor(blockade):
	def __init__(self, pos):
		blockade.__init__(self, long_floor_model,
		                  long_floor_height, long_floor_width, pos)

class portal(sprite):
	def __init__(self, pos, point_to):
		sprite.__init__(self, portal_model, portal_height, portal_width)
		self.x, self.y = pos
		self.dir = point_to

class level_state:
	def __init__(self, player, objects):
		self.sprites = [player]
		self.sprites += objects
		self.exit_game = False
