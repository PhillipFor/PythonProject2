# Version
#0.00
class VersionPF:
	version = '0.04'
	date = '27 Apr 26'
	ver = 'canvas edges - Bullet change direction wall or edge and power'
	text = 'Game - no edges'
	'''
	version
	0.03 26 Apr 26 add you shoot any directiom
	0.02 20 Apr 26 horizontal'
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
		self.x_loc += self.x_move # this loc is canvas not screen
		self.y_loc += self.y_move
		xx, yy = convert(round(self.x_loc), round(self.y_loc))
		self.bullet_rect.center = xx, yy #round(self.x_loc), round(self.y_loc) #wrong
		rect = screen.blit(self.image, self.bullet_rect)
		if self.x_loc > canvas.get_rect().width or self.y_loc > canvas.get_rect().h or self.x_loc < 0 or self.y_loc < 0:
			pass
			bullets.remove(self)
			pass

class Player:
	def __init__(self):
		self.x = canvas.get_rect().width  / 2
		self.y = canvas.get_rect().height  / 2
		self.ccy = screen.get_rect().height / 2
		self.ccx = screen.get_rect().width / 2
		self.a = 0



	def update(self):
		if self.a == 1:
			self.a = 0
		else:
			self.a = 1
			self.x += 0
		self.y += 0
		return self.x, self.y

def convert(xx, yy):
	return canvas, (x, y)

class Screen1:
	def __init__(self):
		pass


	def show(self):

		left = player.y - player.ccy - 1
		top = player.x - player.ccx + 1


		h = screen.get_rect().height
		w = screen.get_rect().width

		if top + screen.get_rect().height == canvas.get_rect().height:
			player.y = top = 0

		if left + screen.get_rect().width == canvas.get_rect().width:
			player.x = left = 0

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
Q: How do I keep the center of a rotated image in place in Pygame
ANS: To keep the center of a rotated image in place, you need to get the center coordinate of the original image’s rectangle and apply that same center coordinate to the rectangle of the newly rotated image before blitting.
'''

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
	x = pygame.mouse.get_pos()[0] - player.ccx
	y = pygame.mouse.get_pos()[1] - player.ccy
	angle = math.degrees(math.atan2(-y, x))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONUP:
			pythag = float(math.sqrt(x ** 2 + y ** 2))
			bullets.append(Bullet(x / pythag, y / pythag, player.x, player.y)) # screen.get_rect().width // 2, screen.get_rect().height // 2))

	screen.fill((255, 255, 255))
	player.update()

	for bullet in bullets:
		bullet.update()
	blitRotateCenter(screen, cannon, ( player.ccx, player.ccy), angle)
	place.show()
	pygame.display.update()
	clock.tick(50)

pygame.quit()
exit()


