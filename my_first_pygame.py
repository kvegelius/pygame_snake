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

	def new_apple_on_board(self, gameBoard, color, snake):
		apple = Apple(1,1)
		apple.set_random_position(gameBoard.get_board_matrix(), snake.get_me_in_board())
		apple_pos = apple.get_my_position()
		apple.init_me_in_board(apple_pos)
		gameBoard.fetch_apple_pos(apple_pos)
		gameBoard.add_to_board(apple, color.red())
		return apple

	def main_loop(self, width, height):

		gameBoard = GameBoard(width, height)
		gameBoard.set_board_matrix(20,20)

		#For now, only print the gameboard
		gameBoard.get_board_matrix()

		color = Color()
		
		square_size = gameBoard.get_pixels_per_square()
		snake = Snake(4,10)
		snake.set_my_length(4)
		snake_pos = snake.get_my_position()
		snake_length = snake.get_my_length()
		print(snake_length, snake_pos)
		snake.init_me_in_board(snake_pos, snake_length)
		gameBoard.add_to_board(snake, color.green())
		
		apple = self.new_apple_on_board(gameBoard, color, snake)

		running = 1

		count = 0
		

		while running:
			if count == 50:
				gameBoard.move_in_matrix(snake)
				if snake.does_collide(apple):
					snake.tail_growing(apple.get_my_position())
					snake.count_eaten_apples()
					print("I have eaten: " +  str(snake.get_eaten_apples()) + " apples!!!")
					apple = self.new_apple_on_board(gameBoard, color, snake)
				elif(snake.touch_my_tail(snake.get_me_in_board()[0])):
					running = 0
				count = 0
			count += 1

			pressed = pygame.key.get_pressed()
			
			for event in pygame.event.get():
				gameBoard.set_dir_state(pressed)
				if event.type == pygame.QUIT or pressed[pygame.K_ESCAPE]:
			 		running = 0

			gameBoard.paint_board()
			pygame.display.flip()



#When running the game add the size of the board in pixels
if __name__ == "__main__":
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	Main(width, height)


