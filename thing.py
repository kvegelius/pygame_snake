#! /usr/bin/env python

import pygame, colors, random

Color = colors.Color

class Thing:

	#size = [pos_x, pos_y, width, height]
	def __init__(self, pos_x, pos_y):
		self.my_position = (pos_x, pos_y)
		self.my_length = 0
		self.color = Color()

	def set_my_position(self, x, y):
		self.my_position = (x, y)

	def get_my_position(self):
		return self.my_position

	def get_me_in_board(self):
		print("snake in board: " + str(self.me_in_board))
		return self.me_in_board

	def set_me_in_board(self, index, elem):
		self.me_in_board[index] = elem

	def get_my_part(self):
		return self.my_part



		# self.rect = pygame.rect.Rect(size)
		# self.size = size

	def draw(self, screen, color, rect):
		pygame.draw.rect(screen, color, rect)

	def does_collide(self, item):
	 	if self.get_me_in_board()[0] == item.get_my_position():
	 		print("CRASCH!!!!!!")
	 		return True
	 		#count apple
	 		#increase speed

	def set_random_position(self, board_matrix, snake_in_board):
		#remember to not put apple on snake_in_board
	 	random_x_board_matrix = random.randint(1, len(board_matrix)-1)
	 	random_y_board_matrix = random.randint(1, len(board_matrix[1])-1)
	 	self.set_my_position(random_x_board_matrix, random_y_board_matrix)
	 	print("set random position: " + str(random_x_board_matrix) + " " + str(random_y_board_matrix))

