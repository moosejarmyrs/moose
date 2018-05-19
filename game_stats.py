class GameStats():
	#Track statistics

	def __init__(self, settings, game_functions):
		#Initialize statistics
		self.settings = settings

		#Start the game in an inactive state
		self.game_active = False
		self.game_paused = False
		
		self.make_cat = False
		
		#Cat stats
		self.catup = False
		self.catdown = False
		self.catright = False
		self.catleft = False
		
		
		