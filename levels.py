from classes import level_state, wall, floor, long_floor, portal
from constants import *

def level1(player):

	player.x = (display_width * 0.1 - player.width * 0.5)
	player.y = (display_height * 0.5 - player.height * 0.5)

	level = level_state(player, [
		floor((display_width * 0.2, floor_y - wall_height)),
		floor((display_width * 0.5, floor_y - wall_height * 2)),
		floor((display_width * 0.7, floor_y - wall_height * 1.8)),
		portal((display_width * 0.8, floor_y - wall_height * 1.8 - player_height), 2)])
	return level

def level2(player):

	player.x = (display_width * 0.9 - player.width * 0.5)
	player.y = (display_height * 0.9 - player.height * 0.5)

	# optimise level

	level = level_state(player, [
		long_floor((0 + player_width, floor_y - wall_height)),

		portal((display_width * 0.8, floor_y - wall_height - player_height), 1)])
	return level
