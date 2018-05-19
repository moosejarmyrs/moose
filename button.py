import sys
import os
import pygame.font

_font_library = {}

class Button():
	def __init__(self, settings, screen, msg, xcord, ycord):
		#Initialize button attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		#Set the dimensions and properties of the button
		self.width, self.height = 200, 50
		self.text_color = (255, 255, 255)
		self.font = self.get_font("fonts/VT323-Regular.ttf", 48)
		
		#Build the button's rect object and center it
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (xcord, ycord)
		
		#The button message needs to be prepped only once
		self.prep_msg(msg)
		
	def get_font(self, path, size):
		global _font_library
		font = _font_library.get(path)
		if font == None:
			canon_path = path.replace("/", os.sep).replace("\\", os.sep)
			font = pygame.font.Font(canon_path, size)
			_font_library[path] = font
		return font
		
	def prep_msg(self, msg):
		#Turn msg into a rendered image and center the text on the button
		self.msg_image = self.font.render(msg, True, self.text_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
		
	def draw_button(self):
		#Draw blank button and then draw image
		self.screen.blit(self.msg_image, self.msg_image_rect)
	
	
	
	
	
	
	
	
	
	
	
