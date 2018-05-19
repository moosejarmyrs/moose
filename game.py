import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from button import Button
import game_functions as gf
from game_functions import *
import game_stats as gs
import samantha
from samantha import *
import cat
from cat import *

settings = Settings()
stats = GameStats(settings, gf)

def run_game():
	#Run the game

	#Basic setup of the game environment
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Cat Game")
	
	screen_rect = screen.get_rect()

	surface = get_image("images/icon.png")

	pygame.display.set_icon(surface)
	bg_color = settings.bg_color

	#Make instances
	sammie = Sammie(settings, screen)
	
	
	i = 0
	
	gf.buttons(screen)
	load_button = Button(settings, screen, "Load", 580, 300)
	new_button = Button(settings, screen, "New", 580, 400)
	quit_button = Button(settings, screen, "Quit", 580, 500)
	
	cats = []
	
	#Main loop
	while True:	
		if stats.game_active == True:
			stats.make_cat = False	
			gf.check_events(settings, screen, stats, load_button, new_button, quit_button, sammie)
			if stats.make_cat:
				gf.make_cat(settings, screen, cats)				
			if cats != []:
				gf.update_screen_cat(settings, screen, stats, sammie, load_button, new_button, quit_button, cats)
				for _cat in cats:
					_cat.update(sammie, _cat, cats, sammie.centerx, sammie.centery)
			else:
				gf.update_screen(settings, screen, stats, sammie, load_button, new_button, quit_button)
			if stats.game_active == True:
				stats.game_paused = False
			sammie.update()

		elif stats.game_active == False:
			if stats.make_cat:
				gf.make_cat(settings, screen)
			
				gf.check_events_cat(settings, screen, stats, load_button, new_button, quit_button, sammie, _cat)
			gf.check_events(settings, screen, stats, load_button, new_button, quit_button, sammie)
			
			if cats != []:
				gf.update_screen_cat(settings, screen, stats, sammie, load_button, new_button, quit_button, cats)
			else:
				gf.update_screen(settings, screen, stats, sammie, load_button, new_button, quit_button)

run_game()
