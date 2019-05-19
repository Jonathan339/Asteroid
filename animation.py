import constants
import os
import pygame
import sys
from pygame.locals import *

class Animation:

	def __init__(self, image, x, y):
		self.image = image
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

	def key_handle(self):
		for event in pygame.event.get():
			if event.type == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
				

	def handle_event(self, event):
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_LEFT:
				self.update('left')
			if event.key == pygame.K_RIGHT:
				self.update('right')
			if event.key == pygame.K_UP:
				self.update('up')
			if event.key == pygame.K_DOWN:
				self.update('down')


	def draw(self):
		surface.blit(self.image, self.rect)
