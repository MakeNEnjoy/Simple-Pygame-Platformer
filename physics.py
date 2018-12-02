from constants import *
from classes import blockade, portal
from levels import level1, level2

def tick(level):
	player = level.sprites[0]

	maybe_x = player.x
	maybe_y = player.y
	relocate_y = False
	relocate_x = False
	allow_jump = True

	if(player.left):
		player.vel_left = run_speed
	else:
		player.vel_left = 0
	if(player.right):
		player.vel_right = run_speed
	else:
		player.vel_right = 0

	player.vel_y += fall_speed
	maybe_y = player.y + player.vel_y

	maybe_x = player.x + player.vel_right - player.vel_left

	if(maybe_y + player.height > floor_y):
		player.y = floor_y - player_height
		player.vel_y = 0
		relocate_y = True
	

	if(maybe_x < 0):
		player.x = 0
		relocate_x = True

	if(maybe_x + player.width > display_width):
		player.x = display_width - player.width
		relocate_x = True


	player_rect = pygame.Rect(maybe_x, maybe_y, player.width, player.height)
	for sprite in level.sprites:
		'''
		Used for blockade collision detection
		'''
		if(isinstance(sprite, blockade)):
			sprite_rect = sprite.getRect()
			if(player_rect.colliderect(sprite_rect)):
				
				if(player.x < sprite.x and player.y + player.height > sprite.y + 1 and player.y < sprite.y + sprite.height - 1):
					#player.x = player.x + ((player.x + player.width) - sprite.x)
					player.x = sprite.x - player.width
					player.vel_right = 0
					relocate_x = True
				if(player.x > sprite.x and player.y + player.height > sprite.y + 1 and player.y < sprite.y + sprite.height - 1):
					#player.x = player.x + (player.x - (sprite.x + sprite.width))
					player.x = sprite.x + sprite.width
					player.vel_left = 0
					relocate_x = True
					
				if(player.y + player.height < sprite.y + 1):
					player.vel_y = 0
					#player.y = player.y + (sprite.y - (player.y + player.height))
					player.y = sprite.y - player.height
					relocate_y = True
				if(player.y > sprite.y + sprite.height):
					player.vel_y = 0
					allow_jump = False
					#player.y = player.y + (sprite.y - (player.y + player.height))
					player.y = sprite.y + sprite.height
					relocate_y = True

		'''
		Used for portal collision detection
		'''
		if(isinstance(sprite, portal)):
			sprite_rect = sprite.getRect()
			if(player_rect.colliderect(sprite_rect)):
				player.level_go_pos = sprite.dir

	if(player.level_go_pos != player.level_pos):
		if(player.level_go_pos == 1):
			level.sprites = level1(player).sprites
		if(player.level_go_pos == 2):
			level.sprites = level2(player).sprites
		player.level_pos = player.level_go_pos
	else:

		if(not relocate_y):
			player.y = maybe_y
		else:
			if(0 <= player.vel_y < 1 and player.jumping and allow_jump):
				player.vel_y = jump_height

		if(not relocate_x):
			player.x = maybe_x
