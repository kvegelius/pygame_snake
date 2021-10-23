#! /usr/bin/env python

import pygame, sys, random, gameBoard, snake, apple, colors
clock = pygame.time.Clock()
Color = colors.Color
GameBoard = gameBoard.GameBoard
Snake = snake.Snake
Apple = apple.Apple


class Main:
	def __init__(self, width, height):
		self.main_loop(width, height)


	# def get_item_position(self, gameBoard, width, height):
	# 	random_x_board_matrix = random.randint(0, gameBoard.get_board_size()[0]-1)
	# 	random_y_board_matrix = random.randint(0, gameBoard.get_board_size()[1]-1)
	# 	pixels_per_square = gameBoard.get_pixels_per_square(width, height) 
	# 	random_x_pos = pixels_per_square[0] * random_x_board_matrix
	# 	random_y_pos = pixels_per_square[1] * random_y_board_matrix

	# 	return (random_x_pos, random_y_pos, random_x_board_matrix, random_y_board_matrix)
	

	def main_loop(self, width, height):

		gameBoard = GameBoard()
		gameBoard.set_board_matrix(20,20)

		screen = pygame.display.set_mode((width, height))
		color = Color()
		screen.fill(color.white())
		
		#For now, only print the gameboard
		gameBoard.get_board_matrix()

		square_size = gameBoard.get_pixels_per_square(width, height)
		snake = Snake(17,10)
		snake.set_my_length(4)
		snake_pos = snake.get_my_position()
		snake_length = snake.get_my_length()
		print(snake_length, snake_pos)
		snake.init_me_in_board(snake_pos, snake_length, screen, square_size)
		#snake_tail_pos = snake.get_me_in_board()[-1]
		#print("snake_tail_pos " + str(snake_tail_pos))
		#snake.draw(screen, color.green(), [snake_tail_pos[1]*square_size[1], snake_tail_pos[0]*square_size[0], square_size[0]*4, square_size[1]])

		apple = Apple(1,1)
		apple_pos = apple.get_my_position()
		apple.init_me_in_board(apple_pos)

		running = 1

		count = 0
		

		while running:
			if count == 100:
				print("bofore move in matrix")
				gameBoard.move_in_matrix(snake, screen)
				count = 0
			count += 1

			pressed = pygame.key.get_pressed()
			
			for event in pygame.event.get():
				gameBoard.set_dir_state(pressed)
				if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
			 		running = 0

			gameBoard.paint_board(width, height, screen)
			pygame.display.flip()

			



		
		


		#square_size = gameBoard.get_pixels_per_square(width, height)

		# random_apple_pos = self.get_item_position(gameBoard, width, height)
		# apple = Apple([random_apple_pos[0], random_apple_pos[1], square_size[0], square_size[1]])
		# gameBoard.set_thing_on_borad(1, (random_apple_pos[2], random_apple_pos[3]))

		# #----WORK IN PROGRESS! Put the apple in the board
		# 
		# apple.set_my_position(random_apple_pos[0], random_apple_pos[1])
		# print("apple position ", str(random_apple_pos[0]))
		# print(apple.get_my_position())

		# random_snake_pos = self.get_item_position(gameBoard, width, height)
		# snake = Snake([random_snake_pos[0], random_snake_pos[1], 5*square_size[0], square_size[1]])
		# gameBoard.set_thing_on_borad(5, (random_snake_pos[2], random_snake_pos[3]))
		# #pygame.display.flip()		


		#while running:
			
			# pressed = pygame.key.get_pressed()
			
			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
			# 		running = 0

			# screen.fill(color.white())

			
			# snake.put_snake_to_opposite_side(width, height)

			# if snake.does_collide(apple) == 0:
			# 	snake.move_me(False)
			# 	apple.draw(screen, color.green())
			# else:
			# 	#snake eats the apple
			# 	random_apple_pos = self.get_item_position(gameBoard, width, height)
			# 	apple = Apple([random_apple_pos[0], random_apple_pos[1], square_size[0], square_size[1]])
			# 	apple.draw(screen, color.green())
			# 	snake.set_velocity(0.9)



			# snake.draw(screen, color.black())
			# snake.handle_keys(pressed)	
			# gameBoard.paint_board(width, height, screen)
			# pygame.display.update()	



#When running the game add the size of the board in pixels
if __name__ == "__main__":
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	Main(width, height)


