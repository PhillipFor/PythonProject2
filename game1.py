class VersionPF:
	version = '0.02'
	date = '12 May 26'
	ver = 'let it move some X spaces'
	text = 'Game - no edges'
	'''
	version
	0.03 12 May 26 let it move some X spaces
	0.02 11 May 26 center Tank
	0.01 10 May 26 bullet remove
	0.00 8 May 26 Games - start
	'''


import pygame
import math
import sys

# Source - https://stackoverflow.com/q/61106297
# Posted by kovels

def cannon():
	image = pygame.Surface((50, 50), pygame.SRCALPHA)
	pygame.draw.rect(image, (100, 100, 100),  (20,0, 10, 20) )            #(30, 17, 25, 15))
	pygame.draw.circle(image, (82, 219, 255), (25, 25), 15)
	return image

class Game:
	def __init__(self):
		self.run = True
		self.screen_width = 1060
		self.screen_height = 798

		self.image = pygame.Surface((10, 10))
		self.image.fill(pygame.Color("whitesmoke"))

		self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
		self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

		self.clock = pygame.time.Clock()

		VersionPF()
		pygame.display.set_caption(
			'Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text + ', ' + VersionPF.ver)
		pygame.display.set_allow_screensaver(True)
		icon = pygame.image.load("img/icon.png")
		pygame.display.set_icon(icon)

		# all_sprites is used to update and draw all sprites together.
		self.all_sprites = pygame.sprite.Group()

		# for collision detection with enemies.
		self.bullet_group = pygame.sprite.Group()

		self.tank = Tank()
		self.all_sprites.add(self.tank)


	def handle_events(self):
		keys = pygame.key.get_pressed()
		self.tank.handle_events()
		if keys[pygame.K_UP]:
			self.tank.move(-1)
		if keys[pygame.K_DOWN]:
			self.tank.move(1)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.run = False
				if event.key == pygame.K_SPACE:
					if len(self.bullet_group.sprites()) <= 10:
						bullet = Bullet(self.tank)
						self.bullet_group.add(bullet)
						self.all_sprites.add(bullet)


	def update(self):
		# Calls `update` methods of all contained sprites.
		self.all_sprites.update()


	def draw(self):
		self.screen.blit(self.image, (0, 0))
		self.all_sprites.draw(self.screen)  # Draw the contained sprites.
		pygame.display.update()


class Tank(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = cannon()
		self.org_image = self.image

		# A nicer way to set the start pos with `get_rect`.
		#self.rect = self.image.get_rect(center=(70, 600))
		self.rect = self.image.get_rect(center=pygame.display.get_surface().get_rect().center)

		self.angle = 0
		self.direction = pygame.Vector2(1, 0)
		self.pos = pygame.Vector2(self.rect.center)
		# x 539 y = 399
		pass

	def handle_events(self):
		pressed = pygame.key.get_pressed()
		if pressed[pygame.K_LEFT]:
			self.angle += 1
		if pressed[pygame.K_RIGHT]:
			self.angle -= 1

		self.direction = pygame.Vector2(1, 0).rotate(-self.angle)
		self.image = pygame.transform.rotate(self.org_image, self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)
		pass

	def move(self, velocity):
		direction = pygame.Vector2(0, velocity).rotate(-self.angle)
		self.pos += direction
		self.rect.center = round(self.pos[0]), round(self.pos[1])
		a = round(self.pos[0])-539
		b = round(self.pos[1])-401
		pass

class Bullet(pygame.sprite.Sprite):
	def __init__(self, tank):
		pygame.sprite.Sprite.__init__(self)
		self.angle = tank.angle
		self.image = pygame.Surface((8,8))
		self.image.fill((255, 0, 0))
		#self.image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.image.get_rect()
		self.pos = pygame.Vector2(tank.pos)
		self.rect.center = round(self.pos.x), round(self.pos.y)
		self.direction = pygame.Vector2(0, -10).rotate(-self.angle)
		self.power = 1000

	def update(self):
		self.pos += self.direction
		self.rect.center = round(self.pos.x), round(self.pos.y)

		self.power -= 1

		if self.rect.left < 0:
			self.direction.x *= -1
			self.rect.left = 0
			self.pos.x = self.rect.centerx
			self.power -= 1
		if self.rect.right > 1060:
			self.direction.x *= -1
			self.rect.right = 1060
			self.pos.x = self.rect.centerx
			self.power -= 1
		if self.rect.top < 0:
			self.direction.y *= -1
			self.rect.top = 0
			self.pos.y = self.rect.centery
			self.power -= 1
		if self.rect.bottom > 798:
			self.direction.y *= -1
			self.rect.right = 798
			self.pos.y = self.rect.centery
			self.power -= 1
		if self.power <= 0:
			game.all_sprites.remove(self)
			game.bullet_group.remove(self)


game = Game()
def main():
	clock = pygame.time.Clock()

	while game.run:
		game.handle_events()
		game.update()
		game.draw()
		clock.tick(60)


def pause(milliseconds, allowesc=True):
	keys = pygame.key.get_pressed()
	current_time = pygame.time.get_ticks()
	wait_time = current_time + milliseconds
	pygame.display.flip()

	while not (current_time > wait_time or (keys[pygame.K_ESCAPE] and allowesc)):
		pygame.event.clear()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_ESCAPE] and allowesc:
			pygame.quit()
			sys.exit()
		current_time = pygame.time.get_ticks()




if __name__ == '__main__':
	main()
	pygame.quit()
	sys.exit()
