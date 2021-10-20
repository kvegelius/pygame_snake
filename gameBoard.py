#! /usr/bin/env python

import pygame, colors, copy, directionController

class GameBoard:
	def __init__(self):
		Color = colors.Color
		self.color = Color()
		self.board_matrix = []
		self.my_width = 0
		self.my_height = 0
		self.board_part = " "
		self.dir_state = "r"
		self.w = 10
		self.h = 10
		self.pixels_per_square_width = 0
		self.pixels_per_square_height = 0
		#self.directionController = DirectionController()

	def get_board_size(self):
		return (self.w, self.h)

	def set_board_matrix(self, w_range, h_range):
		self.mid_list = []
		self.my_width = w_range
		self.my_height = h_range
		for x in range(w_range-1):
			self.mid_list.append(self.board_part)
		for y in range(h_range-1):
			self.board_matrix.append(copy.deepcopy(self.mid_list))


	def get_board_matrix(self):
		for x in self.board_matrix:
			print(x)
		return self.board_matrix

	def get_pixels_per_square(self, screen_width, screen_height):
		self.pixels_per_square_width = screen_width/self.my_width
		self.pixels_per_square_height = screen_height/self.my_height
		return (self.pixels_per_square_width, self.pixels_per_square_height)


	def add_to_board(self, snake, screen):
		snake_in_board = set(snake.get_me_in_board())
		for i in range(len(self.board_matrix)):
			for j in range(len(self.board_matrix[i])):
				if self.board_matrix[i][j] == snake.get_my_part() and (j,i) not in snake_in_board:
					self.board_matrix[i][j] = self.board_part
					snake.draw(screen, self.color.white(), (j*self.pixels_per_square_height, i*self.pixels_per_square_width, self.pixels_per_square_height, self.pixels_per_square_height))
				elif self.board_matrix[i][j] == self.board_part and (j,i) in snake_in_board:
					self.board_matrix[i][j] = snake.get_my_part()
					snake.draw(screen, self.color.green(), (j*self.pixels_per_square_height, i*self.pixels_per_square_width, self.pixels_per_square_height, self.pixels_per_square_height))
							
		#Print board with 
		self.get_board_matrix()

	def move_in_matrix(self, snake, screen):
		#This workds but I don't really understand how...
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
					print(str(elem[0]+snake.get_my_length()) + " <= " + str(self.my_width+1))
					if elem[0]+snake.get_my_length() <= self.my_width+1:
						new_tuple = (elem[0] + 1, elem[1])
					else:
						new_tuple = (0, elem[1])
				elif self.dir_state == "d":
					print(str(elem[1]+snake.get_my_length()) + " <= " + str(self.my_height+1))
					if elem[1]+snake.get_my_length() <= self.my_width+1:
						new_tuple = (elem[0], elem[1]+1)
					else:
						new_tuple = (elem[0], 0)
				elif self.dir_state == "l":
					print(str(elem[0]) + " > " + str(0))
					if elem[0] > 0:
						new_tuple = (elem[0] - 1, elem[1])
					else:
						new_tuple = (self.my_width-2, elem[1])
				elif self.dir_state == "u":
					print(str(elem[1]) + " > " + str(0))
					if elem[1] > 0:
						new_tuple = (elem[0], elem[1]-1)
					else:
						new_tuple = (elem[0], self.my_height-2)
			else:
				new_tuple = remember_old_pos_of_elem
				remember_old_pos_of_elem = elem
			snake.set_me_in_board(index, new_tuple)
			index += 1
		print(snake.get_me_in_board())
		self.add_to_board(snake, screen)

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



		


	
	# def set_thing_on_borad(self, body_squares, position_in_matrix):
	# 	print(body_squares, position_in_matrix)
	# 	x = position_in_matrix[0]
	# 	y = position_in_matrix[1]
	# 	for i in range(0,body_squares):
	# 		self.board_matrix[x][y-i] = "x"

				

	def paint_board(self, screen_width, screen_height, screen):
		pix_per_square = self.get_pixels_per_square(screen_width, screen_height)

		y_index = 1
		for y_array in self.board_matrix:

			y_start = (0, pix_per_square[1]*y_index)
			y_end = (screen_width, pix_per_square[1]*y_index)
			pygame.draw.line(screen, self.color.black(), y_start, y_end, 1)
			y_index += 1
			
			x_index = 1
			for x in y_array:
				x_start = (pix_per_square[0]*x_index, 0)
				x_end = (pix_per_square[0]*x_index, screen_height)
				pygame.draw.line(screen, self.color.black(), x_start, x_end, 1)
				x_index+=1


