import sys
import os
from time import sleep
import pygame
import samantha
from samantha import Sammie
import cat
from cat import Cat
import button
from button import Button
import time
import settings
from settings import Settings
import pygui
from pygui import TextEntry

_image_library = {}
_font_library = {}

def buttons(screen):
	load_button = Button(settings, screen, "Load", 580, 300)
	new_button = Button(settings, screen, "New", 580, 400)
	quit_button = Button(settings, screen, "Quit", 580, 500)

def get_image(path):
		global _image_library
		image = _image_library.get(path)
		if image == None:
			canon_path = path.replace("/", os.sep).replace("\\", os.sep)
			image = pygame.image.load(canon_path)
			_image_library[path] = image
		return image
		
def get_font(path, size):
		global _font_library
		font = _font_library.get(path)
		if font == None:
			canon_path = path.replace("/", os.sep).replace("\\", os.sep)
			font = pygame.font.Font(canon_path, size)
			_font_library[path] = font
		return font

#List of pressed keys
keys = {"right": False, "left": False, "up": False, "down": False}	

def check_keydown_events(event, settings, screen, sammie, stats):
	#Respond to keypresses
	
	#Movement
	if event.key == pygame.K_w:
		keys["up"] = True
		print("Sammie UP: " + str(keys["up"]))
		print("Cat UP: " + str(stats.catup))
	if event.key == pygame.K_a:
		keys["left"] = True
		print("Sammie LEFT: " + str(keys["left"]))
		print("Cat LEFT: " + str(stats.catleft))
	if event.key == pygame.K_s:
		keys["down"] = True
		print("Sammie DOWN: " + str(keys["down"]))
		print("Cat DOWN: " + str(stats.catdown))
	if event.key == pygame.K_d:
		keys["right"] = True
		print("Sammie RIGHT: " + str(keys["right"]))
		print("Cat RIGHT: " + str(stats.catright))
		
	#Other
	if event.key == pygame.K_c:
		stats.make_cat = True

	if event.key == pygame.K_ESCAPE:
		if stats.game_active:
			stats.game_paused = True
			stats.game_active = False
		elif stats.game_paused:
			stats.game_paused = False
			stats.game_active = True
		
def check_keyup_events(event, sammie):
	#Respond to key releases
	if event.key == pygame.K_w:
		keys["up"] = False
	if event.key == pygame.K_a:
		keys["left"] = False
	if event.key == pygame.K_s:
		keys["down"] = False
	if event.key == pygame.K_d:
		keys["right"] = False

		
def do_moving(event, sammie, settings, screen, stats):
	if keys["up"]:
		sammie.up = True
	if not keys["up"]:
		sammie.up = False
	if keys["right"]:
		sammie.right = True
	if not keys["right"]:
		sammie.right = False
	if keys["down"]:
		sammie.down = True
	if not keys["down"]:
		sammie.down = False
	if keys["left"]:
		sammie.left = True
	if not keys["left"]:
		sammie.left = False
		
def do_moving_cat(event, sammie, settings, screen, stats, _cat):
	if keys["up"]:
		sammie.up = True
		_cat.up = True
	if not keys["up"]:
		sammie.up = False
		_cat.up = False
	if keys["right"]:
		sammie.right = True
		_cat.right = True
	if not keys["right"]:
		sammie.right = False
		_cat.right = False
	if keys["down"]:
		sammie.down = True
		_cat.down = True
	if not keys["down"]:
		sammie.down = False
		_cat.down = False
	if keys["left"]:
		sammie.left = True
		_cat.left = True
	if not keys["left"]:
		sammie.left = False
		_cat.left = False
	
def get_sammie_info(sammie, settings, screen, stats, _cat, cats):
	sammiex = sammie.centerx
	sammiey = sammie.centery
	
def get_cat_info(sammie, settings, screen, stats, _cat, cats):
	catx = _cat.centerx
	caty = _cat.centery
		
def check_mouse_events(event, settings, screen, stats, load_button, new_button, quit_button, sammie):
	if event.type == pygame.MOUSEBUTTONDOWN:
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if stats.game_active == False:
			check_buttons(settings, screen, stats, load_button, new_button, quit_button, sammie, mouse_x, mouse_y)
			
	

def check_events(settings, screen, stats, load_button, new_button, quit_button, sammie):
	#Respond to keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, sammie, stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, sammie)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(event, settings, screen, stats, load_button, new_button, quit_button, sammie)
		do_moving(event, sammie, settings, screen, stats)
	
def check_events_cat(settings, screen, stats, load_button, new_button, quit_button, sammie, _cat):
	#Respond to keypresses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, settings, screen, sammie, stats)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, sammie)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			check_mouse_events(event, settings, screen, stats, load_button, new_button, quit_button, sammie)
		do_moving_cat(event, sammie, settings, screen, stats, _cat)
		

def check_buttons(settings, screen, stats, load_button, new_button, quit_button, sammie, mouse_x, mouse_y):
	#Start a new game if the player clicks Play
	quit_button_clicked = quit_button.rect.collidepoint(mouse_x, mouse_y)
	if quit_button_clicked and stats.game_active == False:
		#What to do if Quit button is clicked
		sys.exit()

	load_button_clicked = load_button.rect.collidepoint(mouse_x, mouse_y)
	print("buttons")
	if load_button_clicked and stats.game_active == False:
		#What to do if Load button is clicked
		print("Game loaded!")
		stats.game_active = True
		
	
	new_button_clicked = new_button.rect.collidepoint(mouse_x, mouse_y)
	if new_button_clicked and stats.game_active == False:
		#What to do if New button is clicked
		print("New game!")
		sammie.center_sammie()
		stats.game_active = True
		
def make_cat(settings, screen, cats):
	catcust = TextEntry(0, 0, 2)
	catcust.run(catcust)
	_cat = Cat(settings, screen, catcust.name, catcust.color)
	cats.append(_cat)
	print(_cat.name)
	print(_cat.color)
		
		
def blitme(entity, screen):
	#Draw the object at its current location
	screen.blit(entity.image, entity.rect)

def update_screen(settings, screen, stats, sammie, load_button, new_button, quit_button):
	#Update images on the screen and flip to the new screen
	#Redraw the screen during each pass through the loop
	screen.fill(settings.bg_color)

	blitme(sammie, screen)
	
	#Draw the play button if the game is inactive
	if stats.game_active == False or stats.game_paused == True:
		load_button.draw_button()
		new_button.draw_button()
		quit_button.draw_button()

	#Make the most recently drawn screen visible
	pygame.display.flip()
	
def update_screen_cat(settings, screen, stats, sammie, load_button, new_button, quit_button, cats):
	#Update images on the screen and flip to the new screen
	#Redraw the screen during each pass through the loop
	screen.fill(settings.bg_color)

	blitme(sammie, screen)
	
	for _cat in cats:
		blitme(_cat, screen)

	
	#Draw the play button if the game is inactive
	if stats.game_active == False or stats.game_paused == True:
		load_button.draw_button()
		new_button.draw_button()
		quit_button.draw_button()

	#Make the most recently drawn screen visible
	pygame.display.flip()

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
