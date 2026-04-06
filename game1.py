# Version
#0.00
class VersionPF:
	version = '0.01'
	date = '14 Apr 2026'
	text = 'Game - no edges'
	'''
	version
	try 3
	0.00 1 Apr 2026 Games - start
	'''



import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("3")
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

VersionPF()
pygame.display.set_caption('Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text)
pygame.display.set_allow_screensaver(True)
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)


canvas = pygame.image.load("img/a.jpg")
canvas = pygame.transform.scale(canvas, (2000, 2000))


class Bullet:
	def __init__(self, x_move, y_move, x_loc, y_loc):
		self.image = pygame.Surface((10, 5), pygame.SRCALPHA)
		self.image.fill((255, 0, 0))
		self.image = pygame.transform.rotate(self.image, math.degrees(math.atan2(-y_move, x_move)))
		self.x_move = x_move
		self.y_move = y_move
		self.x_loc = x_loc
		self.y_loc = y_loc
		self.bullet_rect = self.image.get_rect()

	def update(self):
		self.x_loc += self.x_move
		self.y_loc += self.y_move
		self.bullet_rect.center = round(self.x_loc), round(self.y_loc)
		rect = screen.blit(self.image, self.bullet_rect)
		if not screen.get_rect().contains(rect):
			bullets.remove(self)
		if self.x_loc > 800 or self.y_loc > 800:
			bullets.remove(self)


class Player:
	def __init__(self):
		self.x = canvas.get_rect().width / 2
		self.y = canvas.get_rect().height / 2
		self.a = 0

	def update(self):
		self.y = self.y

		#if self.a == 0:
		#	self.a = 1
		#else:
		#	self.a = 0
		self.x += -1
		return self.x, self.y



class Screen1:
	def __init__(self):
		self.scr2 = screen.get_rect().height // 2
		self.scr1 = screen.get_rect().height
		self.bt = canvas.get_rect().height - self.scr1
		self.tp = canvas.get_rect().height + self.scr1
		pass


	def show(self,  x, y):
		if x > canvas.get_rect().height:
			x = 0
			pass
		if x < 0:
			x = canvas.get_rect().height
			pass
		if y > canvas.get_rect().width:
			pass
		if y < 0:
			pass
		sw = 0
		botcnt = 0
		left = y - self.scr2
		top = x - self.scr2
		w = screen.get_rect().width
		h = screen.get_rect().height

		if self.bt < top:
			cnt = (self.bt - top)
			h += cnt
			hh = -cnt
			z = screen.get_rect().height + cnt
			toph = 0
			crop_rect = pygame.Rect(left, toph, w, hh)
			cropped_image1 = canvas.subsurface(crop_rect)
			screen.blit(cropped_image1, (0, z))

		if 0 > top:
			cnt = (self.bt - top)
			h  += cnt
			hh = -cnt
			z = screen.get_rect().height + cnt
			toph = 0
			crop_rect = pygame.Rect(left, toph, w, hh)
			cropped_image1 = canvas.subsurface(crop_rect)
			screen.blit(cropped_image1, (0, z))




		crop_rect = pygame.Rect(left, top, w, h)
		cropped_image = canvas.subsurface(crop_rect)
		screen.blit(cropped_image, (0, 0))








def blitRotateCenter(surf, image, center, angle):
	rotated_image = pygame.transform.rotate(image, angle)
	new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
	surf.blit(rotated_image, new_rect)



cannon = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(cannon, (100, 100, 100), (30, 17, 25, 15))
pygame.draw.circle(cannon, (82, 219, 255), (25, 25), 15)

player = Player()
place = Screen1()
bullet = None
bullets = []
auto_shoot = False
run = True
while run:
	x, y  = pygame.mouse.get_pos()
	x = x - 400
	y = y - 400
	angle = math.degrees(math.atan2(-y, x))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP:
			pythag = float(math.sqrt(x ** 2 + y ** 2))
			bullets.append(Bullet(x / pythag, y / pythag, 400, 400))

	screen.fill((255, 255, 255))
	x, y = player.update()
	place.show(x, y)
	#for bullet in bullets:
	#	bullet.update()
	blitRotateCenter(screen, cannon, (400, 400), angle)
	pygame.display.update()
	clock.tick(50)

pygame.quit()
exit()


