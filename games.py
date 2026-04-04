import sys
import os
import pygame

from Button import Button
from Button import Bnd

# import configparser

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

#creen = pygame.display.set_mode((900,900))
#look_1 = pygame.image.load('img/background.png').convert_alpha()
#look_1 = pygame.transform.scale(look_1, (800, 800))
#pygame.image.save(look_1, 'test.png')

class c:
	screen_width = 800
	screen_height = 800


class v:
	screen = 0
	sizecell = 11
	clock = pygame.time.Clock()
	thegame = 0
	customButton2 = 0
	customButton3 = 0
	canvan = 0


# Configuration
def main():
	v.screen = pygame.display.set_mode((c.screen_width, c.screen_height))
	VersionPF()
	pygame.display.set_caption('Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text)
	pygame.display.set_allow_screensaver(True)
	icon = pygame.image.load("img/icon.png")
	pygame.display.set_icon(icon)
	v.canvas = pygame.Surface((c.screen_width * 2, c.screen_height * 2))

	bg = pygame.image.load("img/background.png")

	v.screen.blit(bg, (0, 0))
	pygame.display.flip()

	Which()


def myFunction():
	pygame.quit()
	sys.exit()


def ggame():
	v.thegame = Bnd.objectsval
	v.customButton2.bnact(0)
	v.customButton3.bnact(0)
	if v.thegame == 1:
		aa = Game(v.screen)
		aa.display()


def Which():
	Button(v.screen, c.screen_width - 100 - 50, 30, 50, 30, 'Exit', myFunction)
	v.customButton2 = Button(v.screen, 50, 30, 150, 30, 'Game 1', ggame, 1)
	v.customButton2.bncolor('', '#aaffaa', '#00ff00')
	v.customButton3 = Button(v.screen, 250, 30, 150, 30, 'Game 2', ggame, 2)
	v.customButton3.bncolor('', '#aaffaa', '#00ff00')
	Bnd.objectsval = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		for a in Bnd.objects:
			a.process()
		if v.thegame != 0:
			break

		pygame.display.flip()
		v.clock.tick(60)


if v.thegame == 1:
	ggame()
	sys.exit()


def parseColour(colour):
	if type(colour) == str:
		# check to see if valid colour
		return pygame.Color(colour)
	else:
		colourRGB = pygame.Color("white")
		colourRGB.r = colour[0]
		colourRGB.g = colour[1]
		colourRGB.b = colour[2]
		return colourRGB


def loadImage(fileName, useColorKey=False):
	if os.path.isfile(fileName):
		image = pygame.image.load(fileName)
		image = image.convert_alpha()
		# Return the image
		return image
	else:
		raise Exception(f"Error loading image: {fileName} – Check filename and path?")


class Background():
	def __init__(self, screen):
		self.screen = screen
		self.colour = pygame.Color("black")
		self.stagePosX = 0
		self.stagePosY = 0
		self.tileWidth = 0
		self.tileHeight = 0


	def setTiles(self, tiles):
		if type(tiles) is str:
			self.tiles = [[loadImage(tiles)]]
		elif type(tiles[0]) is str:
			self.tiles = [[loadImage(i) for i in tiles]]
		else:
			self.tiles = [[loadImage(i) for i in row] for row in tiles]
		self.stagePosX = 0
		self.stagePosY = 0
		self.tileWidth = self.tiles[0][0].get_width()
		self.tileHeight = self.tiles[0][0].get_height()
		self.screen.blit(self.tiles[0][0], [0, 0])
		##  self.surface = self.screen.copy()


	def scroll(self, x, y):
		self.stagePosX = x
		self.stagePosY = y
		col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
		xOff = (0 - self.stagePosX % self.tileWidth)
		row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
		yOff = (0 - self.stagePosY % self.tileHeight)

		col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
		row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
		self.screen.blit(self.tiles[row][col], [xOff, yOff])
		self.screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
		self.screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
		self.screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])


class Game:
	def __init__(self, scr):
		self.screen = scr

	def display(self):
		self.canvas = pygame.Surface((c.screen_width * 2, c.screen_height * 2))

		self.playerX = 0
		self.playerY = 0
		bg = Background(self.screen)
		bg.setTiles("test.png")



		while True:

			bg.scroll(self.playerX, self.playerY)
			self.playerX += 5
			self.playerY += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.flip()
			v.clock.tick(1)


class VersionPF:
	version = '0.01'
	date = '4 Apr 2026'
	text = 'Games - start over'
	'''
	0.00 1 Apr 2026 Games - start
	'''


if __name__ == '__main__':
	main()
