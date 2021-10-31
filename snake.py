#! /usr/bin/env python

import pygame, colors, thing, gameBoard, math

Thing = thing.Thing


class Snake(Thing):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.my_length = 0
		self.me_in_board = []
		self.my_part = "S"
		self.eaten_apples = 0

	def set_my_length(self, length):
		self.my_length = length
		print(self.my_length)

	#we should find out how snake ärver av thing.
	def get_my_length(self):
		print(self.my_length)
		return self.my_length

	def init_me_in_board(self, pos, length):
		for i in range(length):
			self.me_in_board.append((pos[0]-i,pos[1]))
		print("what is this " + str(self.me_in_board))

	def tail_growing(self, apple_pos):
		self.me_in_board.append(apple_pos)

	def count_eaten_apples(self):
		self.eaten_apples += 1

	def get_eaten_apples(self):
		return self. eaten_apples

	def touch_my_tail(self, snake_head):
		print("touch_my_tail: " + str(self.get_me_in_board()) + " " + str(snake_head))
		for index in range(len(self.get_me_in_board())):
			if index != 0:
				if self.get_me_in_board()[index] == snake_head:
					return True

