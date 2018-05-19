import pygame
import game_stats
from game_stats import GameStats
import time

class Cat():
	def __init__(self, settings, screen, name, color):
		#Initialize Cat and set its starting position
		self.screen = screen
		self.settings = settings
		self.name = name
		self.color = color
		
		#Load Cat image and get its rect
		self.image = pygame.image.load("images/cat.png")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		#Start each new Cat at the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		#Store a decimal value for the cat's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#Movement flags
		self.up = False
		self.down = False
		self.right = False
		self.left = False
		
	def update(self, sammie, _cat, cats, sammiex, sammiey):
		#Move cats to follow Sammie
		
		#Distance and direction
		catx = self.centerx
		caty = self.centery
		
		xdif = catx - (catx - sammiex)
		ydif = caty - (caty - sammiey)
		
		direction = 0
		
		if xdif > catx and ydif > caty:
			direction = "Northeast"
		if xdif > catx and ydif < caty:
			direction = "Southeast"
		if xdif < catx and ydif > caty:
			direction = "Northwest"
		if xdif < catx and ydif < caty:
			direction = "Southwest"
		
		if direction == 0:
			self.down = False
			self.up = False
			self.left = False
			self.right = False
		
		if direction == "Southwest":
			self.down = True
			self.left = True
			self.up = False
			self.right = False
		if direction == "Northwest":
			self.up = True
			self.left = True
			self.down = False
			self.right = False
		if direction == "Southeast":
			self.down = True
			self.right = True
			self.up = False
			self.left = False
		if direction == "Northeast":
			self.up = True
			self.right = True
			self.down = False
			self.left = False
		
		
			
		if self.up and self.rect.top > self.screen_rect.top:
			self.centery += self.settings.cat_speed_factor + 0.1
			if self.right and self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.cat_speed_factor/8
			elif self.left and self.rect.left > 0:
				self.centerx -= self.settings.cat_speed_factor/8
				
		if self.down and self.rect.bottom < self.screen_rect.bottom:
			self.centery -= self.settings.cat_speed_factor + 0.1
			if self.right and self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.cat_speed_factor/8
			elif self.left and self.rect.left > 0:
				self.centerx -= self.settings.cat_speed_factor/8
				
		if self.right and self.rect.right < self.screen_rect.right:
			self.centerx += self.settings.cat_speed_factor + 0.1
			if self.up and self.rect.top < self.screen_rect.top:
				self.centery += self.settings.cat_speed_factor/8
			elif self.down and self.rect.bottom > self.screen_rect.bottom:
				self.centery -= self.settings.cat_speed_factor/8
				
		if self.left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.settings.cat_speed_factor + 0.1
			if self.up and self.rect.top < self.screen_rect.top:
				self.centery += self.settings.cat_speed_factor/8
			elif self.down and self.rect.bottom > self.screen_rect.bottom:
				self.centery -= self.settings.cat_speed_factor/8
		
		
		#Update rect object from self.center
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
		
	def center_cat(self):
		#Center Cat on the screen
		self.center = self.screen_rect.centerx, self.screen_rect.centery
		
	def sayname(self):
		print(self.name)
		
		
		
