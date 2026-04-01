# Imports
import pygame, sys, os

pygame.init()

bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
bg = pygame.transform.scale(bg, (500,500))



pygame.image.save(bg, 'test.png')

sys.exit()

