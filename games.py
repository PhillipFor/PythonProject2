import sys
import os
import pygame

from Button import Button
from Button import Bnd

#import configparser

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

font = pygame.font.SysFont('Arial', 24)


class bs:
    screen_width = 800
    screen_height = 600
    screen = 0
    sizecell = 10
    clock = pygame.time.Clock()
    thegame = 0
    customButton2 = 0
    customButton3 = 0

# Configuration
def main():
    bs.screen =  pygame.display.set_mode((bs.screen_width, bs.screen_height))
    VersionPF()
    pygame.display.set_caption('Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text)
    #pygame.display.set_allow_screensaver(True)
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)

    Which()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        pygame.display.flip()
        bs.clock.tick(60)


def myFunction():
    pygame.quit()
    sys.exit()



def Which():
    Button(bs.screen,bs.screen_width - 100 - 50, 30, 50, 30, 'Exit', myFunction)
    bs.customButton2 = Button(bs.screen, 50, 30, 150, 30, 'Game 1', ggame, 1)
    bs.customButton2.bncolor('', '#aaffaa', '#00ff00')
    bs.customButton3 = Button(bs.screen, 250, 30, 150, 30, 'Game 2', ggame, 2)
    bs.customButton3.bncolor('', '#aaffaa', '#00ff00')
    Bnd.objectsval = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if bs.thegame != 0:
            break
        for a in Bnd.objects:
            a.process()

        pygame.display.flip()
        bs.clock.tick(60)

def ggame():
    bs.thegame = Bnd.objectsval
    bs.customButton2.act(False)
    bs.customButton3.act(False)



# Game loop.
class Board:
    def __init__(self, screen):

        pass

    def draw(self):
        pass

class Game:
    def __init__(self, screen):
        while True:
            bs.screen.fill(20, 20, 20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for a in Bnd.objects:
                a.process()

                pygame.display.flip()
                bs.clock.tick(60)


class VersionPF:
    version = '0.01'
    date = '1 Apr 2026'
    text = 'Games - start over'
    '''
    0.00 21 Feb 2026 Games - start
    '''

if __name__ == '__main__':
   main()
