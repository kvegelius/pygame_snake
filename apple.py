#! /usr/bin/env python

import thing

Thing = thing.Thing

class Apple(Thing):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.my_part = "A"
		self.me_in_board = []

	def init_me_in_board(self, pos):
		self.me_in_board.append((pos[0],pos[1]))
		print("what is this " + str(self.me_in_board))
