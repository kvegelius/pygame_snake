#! /usr/bin/env python

import pygame, colors, copy, directionController, apple

Color = colors.Color
Apple = apple.Apple

class GameBoard:
	def __init__(self, screen_width, screen_height):
		self.color = Color()
		self.board_matrix = []
		self.my_width = 0
		self.my_height = 0
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.board_part = " "
		self.dir_state = "r"
		self.w = 10
		self.h = 10
		self.pixels_per_square_width = 0
		self.pixels_per_square_height = 0
		
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.screen.fill(self.color.white())

		self.apple_pos = ()

	def get_board_size(self):
		return (self.w, self.h)

	def set_board_matrix(self, w_range, h_range):
		self.mid_list = []
		self.my_width = w_range
		self.my_height = h_range
		for x in range(w_range):
			self.mid_list.append(self.board_part)
		for y in range(h_range):
			self.board_matrix.append(copy.deepcopy(self.mid_list))


	def get_board_matrix(self):
		for x in self.board_matrix:
			print(x)
		return self.board_matrix

	def get_pixels_per_square(self):
		self.pixels_per_square_width = self.screen_width/self.my_width
		self.pixels_per_square_height = self.screen_height/self.my_height
		return (self.pixels_per_square_width, self.pixels_per_square_height)

	def fetch_apple_pos(self, pos):
		self.apple_pos = pos

	def add_to_board(self, thing, color_func):
		snake_in_board = set(thing.get_me_in_board())

		for i in range(len(self.board_matrix)):
			for j in range(len(self.board_matrix[i])):
				if self.board_matrix[i][j] == thing.get_my_part() and (j,i) not in snake_in_board:
					self.board_matrix[i][j] = self.board_part
					thing.draw(self.screen, self.color.white(), (j*self.pixels_per_square_height, i*self.pixels_per_square_width, self.pixels_per_square_height, self.pixels_per_square_height))
				elif self.board_matrix[i][j] == self.board_part and (j,i) in snake_in_board:
					self.board_matrix[i][j] = thing.get_my_part()
					thing.draw(self.screen, color_func, (j*self.pixels_per_square_height, i*self.pixels_per_square_width, self.pixels_per_square_height, self.pixels_per_square_height))
							
		#Print board with 
		self.get_board_matrix()

	def move_in_matrix(self, snake):
		snake_in_board = snake.get_me_in_board()
		index = 0
		new_tuple = ()
		print(self.dir_state + " is the state")
		remember_old_pos_of_elem = ()
		for elem in snake_in_board:
			print("elem is: " + str(elem))
			if remember_old_pos_of_elem == ():
				print("is first elem: " + str(elem))
				remember_old_pos_of_elem = elem
				if self.dir_state == "r":
					print(str(elem[0]) + " < " + str(self.my_width-1))
					if elem[0] < self.my_width-1:
						new_tuple = (elem[0] + 1, elem[1])
					else:
						new_tuple = (0, elem[1])
				elif self.dir_state == "d":
					print(str(elem[1]) + " < " + str(self.my_height-1))
					if elem[1] < self.my_height-1:
						new_tuple = (elem[0], elem[1]+1)
					else:
						new_tuple = (elem[0], 0)
				elif self.dir_state == "l":
					print(str(elem[0]) + " > " + str(0))
					if elem[0] > 0:
						new_tuple = (elem[0] - 1, elem[1])
					else:
						new_tuple = (self.my_width-1, elem[1])
				elif self.dir_state == "u":
					print(str(elem[1]) + " > " + str(0))
					if elem[1] > 0:
						new_tuple = (elem[0], elem[1]-1)
					else:
						new_tuple = (elem[0], self.my_height-1)
			else:
				new_tuple = remember_old_pos_of_elem
				remember_old_pos_of_elem = elem
			snake.set_me_in_board(index, new_tuple)
			index += 1
		print(snake.get_me_in_board())
		self.add_to_board(snake, self.color.green())

	def set_dir_state(self, key):
		if key[pygame.K_LEFT] and self.dir_state != "r":
			print("left")
			self.dir_state = "l"
		if key[pygame.K_RIGHT] and self.dir_state != "l":
			print("right")
			self.dir_state = "r"
		if key[pygame.K_UP] and self.dir_state != "d":
			print("up")
			self.dir_state = "u"
		if key[pygame.K_DOWN] and self.dir_state != "u":
			print("down")
			self.dir_state = "d"

	def get_dir_state(self):
		return self.dir_state
				

	def paint_board(self):
		pix_per_square = self.get_pixels_per_square()

		y_index = 1
		for y_array in self.board_matrix:

			y_start = (0, pix_per_square[1]*y_index)
			y_end = (self.screen_width, pix_per_square[1]*y_index)
			pygame.draw.line(self.screen, self.color.black(), y_start, y_end, 1)
			y_index += 1
			
			x_index = 1
			for x in y_array:
				x_start = (pix_per_square[0]*x_index, 0)
				x_end = (pix_per_square[0]*x_index, self.screen_height)
				pygame.draw.line(self.screen, self.color.black(), x_start, x_end, 1)
				x_index+=1


