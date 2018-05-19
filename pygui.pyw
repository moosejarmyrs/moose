#Basic python library to add GUI elements to Pygame
import pygame
from tkinter import *
import time

class Title(Frame):
	def __init__(self, parent = None):
		Frame.__init__(self, parent)
		self.parent = parent
		self.title()
	def title(self):
		self.winfo_toplevel().title("Create Cat")

class TextEntry():
	def __init__(self, xcord, ycord, numEntries):
		#Initialize all variables
		self.xcord = xcord
		self.ycord = ycord
		self.numEntries = numEntries
		
		#Create new Tkinter window
		self.root = Tk()
		self.root.iconbitmap("images/icon.ico")
		title = Title(self.root)
		self.root.geometry("300x300")
		self.root.resizable(False, False)
		
		#Create Tk Frames
		self.topF = Frame(self.root)
		self.topF.grid(row = 0, column = 0)
		self.botF = Frame(self.root)
		self.botF.grid(row = 0, column = 0)
		
	def make_assets(self, topF):
		
		#Create TextEntry assets
		self.namelabel = Label(self.topF, text = "Name: ")
		self.namelabel.grid(row = 0, column = 0)
		self.nameEntry = Entry(self.topF)
		self.nameEntry.grid(row = 0, column = 1)
		self.nameEntry.focus_force()
		
		self.colorlabel = Label(self.topF, text = "Color: ")
		self.colorlabel.grid(row = 1, column = 0)
		self.colorEntry = Entry(self.topF)
		self.colorEntry.grid(row = 1, column = 1)
		
	def done(self):
		file = open("cats.py", "+a")
		file.write("\ncatnames.append(\"" + self.nameEntry.get() + "\")")
		file.write("\ncatcolors.append(\"" + self.colorEntry.get() + "\")")
		file.close()
		
		self.name = self.nameEntry.get()
		self.color = self.colorEntry.get()
		
		self.root.destroy()
		
	def button(self):
		self.goButton = Button(self.topF, text = "Go", command = self.done)
		self.goButton.grid(row = 2, column = 0)	
		
		self.root.mainloop()

	def run(self, title):
		title.make_assets(title.topF)
		title.button()
