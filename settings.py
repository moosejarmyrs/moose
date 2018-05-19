class Settings():
	#A class to store all settings for cat game

	def __init__(self):
		#Initialize the game's settings
		self.screen_width = 1160
		self.screen_height = 800
		self.bg_color = (160, 60, 60)
		
		#Sammie settings
		self.sammie_speed_factor = 0.25
		
		#Cat settings
		self.cat_speed_factor = 0.10

