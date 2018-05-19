import pygame

class Sammie():
	def __init__(self, settings, screen):
		#Initialize Sammie and set its starting position
		self.screen = screen
		self.settings = settings
		
		#Load Sammie image and get its rect
		self.image = pygame.image.load("images/sammie.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Start Sammie at the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		#Store a decimal value for sammie's center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		#Movement flags
		self.up = False
		self.down = False
		self.right = False
		self.left = False
		
	def update(self):
		#Move Sammie up down right or left
		if self.up and self.rect.top > self.screen_rect.top:
			self.centery -= self.settings.sammie_speed_factor + 0.1
			if self.right and self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.sammie_speed_factor/8
			elif self.left and self.rect.left > 0:
				self.centerx -= self.settings.sammie_speed_factor/8
				
		if self.down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.settings.sammie_speed_factor + 0.1
			if self.right and self.rect.right < self.screen_rect.right:
				self.centerx += self.settings.sammie_speed_factor/8
			elif self.left and self.rect.left > 0:
				self.centerx -= self.settings.sammie_speed_factor/8
				
		if self.right and self.rect.right < self.screen_rect.right:
			self.centerx += self.settings.sammie_speed_factor + 0.1
			if self.up and self.rect.top < self.screen_rect.top:
				self.centery -= self.settings.sammie_speed_factor/8
			elif self.down and self.rect.bottom > self.screen_rect.bottom:
				self.centery += self.settings.sammie_speed_factor/8
				
		if self.left and self.rect.left > self.screen_rect.left:
			self.centerx -= self.settings.sammie_speed_factor + 0.1
			if self.up and self.rect.top < self.screen_rect.top:
				self.centery -= self.settings.sammie_speed_factor/8
			elif self.down and self.rect.bottom > self.screen_rect.bottom:
				self.centery += self.settings.sammie_speed_factor/8
		
		#Update rect object from self.center
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		
	def center_sammie(self):
		#Center Sammie on the screen
		self.center = self.screen_rect.centerx, self.screen_rect.centery
		
		
		
		
		
