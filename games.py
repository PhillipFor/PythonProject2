import sys
import os
import pygame
from pygame.locals import *
import configparser

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

font = pygame.font.SysFont('Arial', 24)


class bs:
    screen = None
    screen_width = 1000
    screen_height = 900
    sizecell = 10
    clock = pygame.time.Clock()
    thegame = 0

# Configuration
def main():
    bs.screen =  pygame.display.set_mode((bs.screen_width, bs.screen_height))
    VersionPF()
    pygame.display.set_caption('Version ' + VersionPF.version + ' ' + VersionPF.date + '  ' + VersionPF.text)
    #pygame.display.set_allow_screensaver(True)
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)

    Which()
    stop()

    board = Board(bs.screen)
    gsm = Game(board)
    pass

def stop():
      while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Bnd:
    objects = []
    objectsval = 0


class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, val=None):
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
        bs.screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    pygame.quit()
    sys.exit()


def ggame():
    bs.thegame = Bnd.objectsval
    Button.customButton2.active(False)
    Button.customButton3.active(False)


def Which():
    customButton1 = Button(bs.screen_width - 100 - 50, 30, 50, 30, 'Exit', myFunction)
    Button.customButton2 = Button(50, 30, 150, 30, 'Game 1', ggame, 1)
    Button.customButton2.bncolor('', '#aaffaa', '#00ff00')
    Button.customButton3 = Button(250, 30, 150, 30, 'Game 2', ggame, 2)
    Button.customButton3.bncolor('', '#aaffaa', '#00ff00')
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


# Game loop.
class Board:
    def __init__(self, screen):

        pass



class Game:
    def __init__(self, screen):
        while True:
            bs.screen.fill((20, 20, 20))
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
    date = '4 Mar 2026'
    text = 'Games - start'
    '''
    0,00 21 Feb 2026 Games - start
    
    '''

if __name__ == '__main__':
    main()



