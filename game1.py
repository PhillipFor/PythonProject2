class VersionPF:
	version = '0.04'
	date = '1 May 26'
	ver = 'canvas edges'
	text = 'Game - no edges'
	'''
	version
	0.03 26 Apr 26 add you shoot any direction
	0.02 20 Apr 26 horizontal'
	0.01 17 Apr 26 try 4
	0.00 1 Apr 26 Games - start
	'''


import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

VersionPF()
pygame.display.set_caption(
	'Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text + ', ' + VersionPF.ver)
pygame.display.set_allow_screensaver(True)
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

canvas = pygame.image.load("img/a.jpg").convert()
canvas_org = pygame.transform.scale(canvas, (2000, 2000))



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
		self.x_loc += self.x_move  # this loc is canvas not screen
		self.y_loc += self.y_move
		self.bullet_rect.center = round(self.x_loc), round(self.y_loc)
		canvas.blit(self.image, self.bullet_rect)
		if self.x_loc > canvas.get_rect().width or self.y_loc > canvas.get_rect().h or self.x_loc < 0 or self.y_loc < 0:
			pass
			bullets.remove(self)
			pass


class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x, y))
        self.angle = 0
    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.angle = (self.angle + 1) % 360



class Player1:
	def __init__(self):
		a = canvas_org.width / 2
		self.x = self.ccx = canvas_org.width / 2
		self.y = self.ccy = canvas_org.height / 2
		self.sx = screen.get_rect().width
		self.sy = screen.get_rect().height

		self.scx = screen.get_rect().width / 2
		self.scy = screen.get_rect().height / 2
		self.a = 0




def pause(milliseconds, allowesc=True):
	keys = pygame.key.get_pressed()
	current_time = pygame.time.get_ticks()
	waittime = current_time + milliseconds
	pygame.display.flip()

	while not (current_time > waittime or (keys[pygame.K_ESCAPE] and allowesc)):
		pygame.event.clear()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE] and allowesc:
			pygame.quit()
			sys.exit()
		current_time = pygame.time.get_ticks()


class Screen1:
	def __init__(self):
		pass

	def update(self):
		pass

	def show(self):
		top = player1.x - player1.scx
		left = player1.y - player1.scy



		h = screen.get_rect().height
		w = screen.get_rect().width
		if top + screen.get_rect().height == canvas.get_rect().height:
			player1.y = top = 0

		if left + screen.get_rect().width == canvas.get_rect().width:
			player1.x = left = 0

		if top == -1:
			player.y = top = canvas.get_rect().height - screen.get_rect().height - 1

		if left == -1:
			player.x = left = canvas.get_rect().width - screen.get_rect().width - 1

		cropped_rect = pygame.Rect(left, top, w, h)
		cropped_image = canvas.subsurface(cropped_rect)
		screen.blit(cropped_image, (0, 0))


def blitRotateCenter(surf, image, center, angle):
	rotated_image = pygame.transform.rotate(image, angle)
	new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
	surf.blit(rotated_image, new_rect)


'''
Q: How do I keep the center of a rotated image in place in pygame
ANS: To keep the center of a rotated image in place, you need to get the center coordinate of the original image’s rectangle and apply that same center coordinate to the rectangle of the newly rotated image before blitting.
'''

canvas_wall = canvas_org.copy()
#add walll here


player1 = Player1()
place = Screen1()


surface = pygame.Surface((100, 50), pygame.SRCALPHA)
surface.fill("black")
player = Player(surface, *screen.get_rect().center)
all_sprites = pygame.sprite.Group(player)

cannon = pygame.Surface((50, 50), pygame.SRCALPHA)
pygame.draw.rect(cannon, (100, 100, 100), (30, 17, 25, 15))
pygame.draw.circle(cannon, (82, 219, 255), (25, 25), 15)

bullet = None
bullets = []
auto_shoot = False

run = True

while run:
	canvas = canvas_wall.copy()
	a = pygame.mouse.get_pos()[0]
	x = pygame.mouse.get_pos()[0] - player1.scx
	y = pygame.mouse.get_pos()[1] - player1.scy
	angle = math.degrees(math.atan2(-y, x))
	if  a != 0:
		pass
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP and a != 0:
			pythag = float(math.sqrt(x ** 2 + y ** 2))
			bullets.append(Bullet(x / pythag, y / pythag, screen.get_rect().width // 2, screen.get_rect().height // 2))

	screen.fill((255, 255, 255))

	player.update()

	for bullet in bullets:
		bullet.update()


	place.show()
	all_sprites.update()
	pygame.display.flip()
	clock.tick(50)

pygame.quit()
exit()
