#! /usr/bin/env python

import pygame, colors, thing, gameBoard, math

Thing = thing.Thing


class Snake(Thing):
	def __init__(self, pos_x, pos_y):
		super().__init__(pos_x, pos_y)
		self.my_length = 0
		self.me_in_board = []
		self.my_part = "S"

	def set_my_length(self, length):
		self.my_length = length
		print(self.my_length)

	#we should find out how snake ärver av thing.
	def get_my_length(self):
		print(self.my_length)
		return self.my_length

	def init_me_in_board(self, pos, length, screen, square_size):
		for i in range(length):
			self.me_in_board.append((pos[0]-i,pos[1]))
		#self.draw(screen, self.color.green(), (self.me_in_board[-1][0]*square_size[1], pos[1]*square_size[0], length*square_size[1], square_size[0]))
		print("what is this " + str(self.me_in_board))

	def get_me_in_board(self):
		print("snake in board: " + str(self.me_in_board))
		return self.me_in_board

	def set_me_in_board(self, index, elem):
		self.me_in_board[index] = elem

	def get_my_part(self):
		return self.my_part

	



	#velocity = 1
	#eaten_apples = 0
	
	

	#def move(self, x, y):
	#	self.rect.move_ip(x, y)
	#	pass

	# def handle_keys(self, key):
	# 	v = 5
	# 	if key[pygame.K_LEFT]:
	# 		self.rect.move_ip(-v, 0)
	# 		#pass
	# 	if key[pygame.K_RIGHT]:
	# 		self.rect.move_ip(v, 0)
	# 		#pass
	# 	if key[pygame.K_UP]:
	# 		up = self.size[1]
	# 		self.rect.move_ip(0, -v)
	# 		#pass
	# 	if key[pygame.K_DOWN]:
	# 		self.rect.move_ip(0, v)
	# 		#pass

	# def set_velocity(self, acc):
	# 	self.eaten_apples += 1
	# 	self.velocity = self.velocity + math.pow(acc, self.eaten_apples)
	# 	self.move_me(self.velocity)

	# def get_velocity(self):
	# 	return self.velocity

	# def move_me(self, new_v):
	# 	if new_v:
	# 		self.velocity = new_v
	# 	#self.rect.move_ip(self.velocity, 0)

	# def put_snake_to_opposite_side(self, width, height):
	# 	snake_width = self.rect.width 
	# 	if self.rect.right > (width + snake_width):
	# 		print("To the right of the screen")
	# 		self.move(-(width+snake_width), 0)	
	# 	elif (self.rect.left + snake_width) < 0:
	# 		print("To the left of the screen ")
	# 		self.move(width+snake_width, 0)
	# 	elif self.rect.top > height:
	# 		print("Below the screen")
	# 		self.move(0, -height)
	# 	elif self.rect.bottom < 0:
	# 		print("Above the screen ")
	# 		self.move(0, height)