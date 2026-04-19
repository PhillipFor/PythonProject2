# Version
#0.00
class VersionPF:
	version = '0.02'
	date = '18 Apr 26'
	ver = 'horizontal'
	text = 'Game - no edges'
	'''
	version
	0.01 17 Apr 26 try 4
	0.00 1 Apr 26 Games - start
	'''



import pygame
import math

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

VersionPF()
pygame.display.set_caption('Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text + ', ' + VersionPF.ver)
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
		self.y = 600
		#  canvas.get_rect().width # / 2
		self.x = canvas.get_rect().height  / 2
		self.a = 0

	def update(self):
		#if self.a == 0:
		#	self.a = 1
		#else:
		#	self.a = 0
		self.y += -1
		return self.x, self.y



class Screen1:
	def __init__(self):
		pass


	def show(self):

		left = player.y
		top = player.x


		w = screen.get_rect().width
		h = screen.get_rect().height




		if top == -screen.get_rect().height:
			top = top + canvas.get_rect().height
			player.x = top
		if top > canvas.get_rect().height:
			top = top - canvas.get_rect().height
			player.x = top

		if left == -screen.get_rect().width:
			left = left + canvas.get_rect().width
			player.y = left
		if left > canvas.get_rect().width:
			left = left - canvas.get_rect().width
			player.y = left


######################################################
		right = 0
		rdl = 0

		if top < 0:
			top = 0
		if left < 0:
			c = abs(left)
			right = canvas.get_rect().width - c
			wr = c
			left = 0
			w = w - c
			rdl = c

		crop_rect = pygame.Rect(left, top, w, h)
		cropped_image = canvas.subsurface(crop_rect)
		screen.blit(cropped_image, (rdl, 0))

		if right != 0:
			crop_rect = pygame.Rect(right, top, wr, h)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, 0))


		##############################################
		'''
		if top < 0:
			cnt = -top

			hh = cnt
			bh =  canvas.get_rect().height - cnt

			crop_rect = pygame.Rect(left, bh, w, hh)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, 0))

			ch = h - cnt
			top = 0

			crop_rect = pygame.Rect(left, top, w, ch)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, cnt))

		elif top > (canvas.get_rect().height - screen.get_rect().height):
			cnt = top - (canvas.get_rect().height - screen.get_rect().height)

			bt = 0
			zz = screen.get_rect().height - cnt

			crop_rect = pygame.Rect(left, bt, w, cnt)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, zz))

			h = zz

			crop_rect = pygame.Rect(left, top, w, h)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, 0))


		else:
			crop_rect = pygame.Rect(left, top, w, h)
			cropped_image = canvas.subsurface(crop_rect)
			screen.blit(cropped_image, (0, 0))

'''






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
	#x, y  = pygame.mouse.get_pos()

	angle = math.degrees(math.atan2(-player.y, player.x))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP:
			pythag = float(math.sqrt(player.x ** 2 + player.y ** 2))
			bullets.append(Bullet(player.x / pythag, player.y / pythag, screen.get_rect().height // 2, screen.get_rect().width // 2))

	screen.fill((255, 255, 255))
	player.update()
	place.show()
	#for bullet in bullets:
	#	bullet.update()
	#blitRotateCenter(screen, cannon, (400, 400), angle)
	pygame.display.update()
	clock.tick(50)

pygame.quit()
exit()


