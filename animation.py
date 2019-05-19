import constants
import os
import pygame
import sys
from pygame.locals import *

class Animation:

	def __init__(self, image, x, y):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.top, self.rect.left = 500, 300
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 0
		self.key = []

	def update(self, direction):
		if direction == 'left':
			self.clip(self.left_states)
			self.rect.x -= 5
		if direction == 'right':
			self.clip(self.right_states)
			self.rect.x += 5
		if direction == 'up':
			self.clip(self.up_states)
			self.rect.y -= 5
		if direction == 'down':
			self.clip(self.down_states)
			self.rect.y += 5

	def move(self):
		self.x += self.vx
		self.y += self.vy

	

	def draw(self, surface):
		surface.blit(self.image, (self.x, self.y))
