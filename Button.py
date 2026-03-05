import pygame


class Bnd:
	objects = []
	objectsval = 0


class Button:
	def __init__(self, screen, x, y, width, height, buttonText='Button', onclickFunction=None, val=None):
		self.screen = screen
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.onclickFunction = onclickFunction
		self.val = val
		self.font = pygame.font.SysFont('Arial', 24)
		self.act = True
		self.col = '#000000'
		self.fillColors = {
			'normal': '#ffffff',
			'hover': '#aaaaaa',
			'pressed': '#333333',
		}

		self.buttonSurface = pygame.Surface((self.width, self.height))
		self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

		self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

		self.alreadyPressed = False

		Bnd.objects.append(self)

	def bncolor(self, nor='#ffffff', hov='#aaaaaa', pres='#333333'):
		if nor != '':
			self.fillColors['normal'] = nor
		if hov != '':
			self.fillColors['hover'] = hov
		if pres != '':
			self.fillColors['pressed'] = pres

	def bntext(self,txt):
		self.buttonSurf = self.font.render(txt, True, (20, 20, 20))

	def active(self, val, col=''):
		self.act = val
		if col != '':
			self.col = col
		self.process()

	def process(self):
		if not self.act:
			self.buttonSurface.fill(self.col)
		else:
			mousePos = pygame.mouse.get_pos()

			self.buttonSurface.fill(self.fillColors['normal'])
			if self.buttonRect.collidepoint(mousePos):
				self.buttonSurface.fill(self.fillColors['hover'])

				if pygame.mouse.get_pressed(num_buttons=3)[0]:
					self.buttonSurface.fill(self.fillColors['pressed'])

					if not self.alreadyPressed:
						Bnd.objectsval = self.val
						self.onclickFunction()
						self.alreadyPressed = True

				else:
					self.alreadyPressed = False

		self.buttonSurface.blit(self.buttonSurf, [
			self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
			self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
		])
		self.screen.blit(self.buttonSurface, self.buttonRect)

