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

# Configuration
def main():
    bs.screen =  pygame.display.set_mode((bs.screen_width, bs.screen_height))
    VersionPF()
    pygame.display.set_caption('Version' + VersionPF.version + ' ' + VersionPF.date )
    #pygame.display.set_allow_screensaver(True)
    icon = pygame.image.load("img/icon.png")
    pygame.display.set_icon(icon)

    board = Board(bs.screen)
    gsm = Game(board)
    pass

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

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        Bnd.objects.append(self)

    def bncolor(self, nor, hov='#666666'):
        self.fillColors['normal'] = nor
        self.fillColors['hover'] = hov

    def bntext(self,txt):
        self.buttonSurf = self.font.render(txt, True, (20, 20, 20))


    def process(self):

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


def Game1():
    Button.customButton2.bncolor('#00ff00')
    Button.customButton2.bntext('Reset game 1')
    Button.customButton3.bncolor('#ffffff')
    Button.customButton3.bntext('Game 2')

def Game2():
    Button.customButton3.bncolor('#00ff00')
    Button.customButton3.bntext('Reset game 2')
    Button.customButton2.bncolor('#ffffff')
    Button.customButton2.bntext('Game 1')




# Game loop.
class Board:
    def __init__(self, screen):

        customButton1 = Button(bs.screen_width - 100 - 50, 30, 100, 30, 'Exit', myFunction)
        Button.customButton2 = Button(50, 30, 150, 30, 'Game 1', Game1)
        Button.customButton3 = Button(250, 30, 150, 30, 'Game 2', Game2)

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
    date = '24 Feb 2026'
    text = 'Games - start'
    '''
    0,00 21 Feb 2026 Games - start
    
    '''

if __name__ == '__main__':
    main()



