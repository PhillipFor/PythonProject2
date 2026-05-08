class VersionPF:
	version = '0.04'
	date = '7 May 26'
	ver = 'different bullets and player'
	text = 'Game - no edges'
	'''
	version
	--- 8 May 26 GAVE UP
	0.04 1 May 26 different bullet
	0.03 26 Apr 26 add you shoot any direction
	0.02 20 Apr 26 horizontal'
	0.01 17 Apr 26 try 4
	0.00 1 Apr 26 Games - start
	'''


import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))






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

class make_cannon:
	cannon = pygame.Surface((50, 50), pygame.SRCALPHA)
	pygame.draw.rect(cannon, (100, 100, 100), (30, 17, 25, 15))
	pygame.draw.circle(cannon, (82, 219, 255), (25, 25), 15)


pygame.quit()
exit()
