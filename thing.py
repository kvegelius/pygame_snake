#! /usr/bin/env python

import pygame, colors

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

	# def does_collide(self, item):
	# 	return self.rect.colliderect(item.get_self())

	# def get_self(self):
	# 	return self.rect