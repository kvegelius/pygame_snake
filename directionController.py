#! /usr/bin/env python

import pygame

#For now this is not used
class DirectionController:
	def __init__(self):
		self.dir_state = "r"

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

