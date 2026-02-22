
import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 1000, 900
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont('Arial', 40)



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

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        Bnd.objects.append(self)

    def bncolor(self, nor, hov='#666666'):
        self.fillColors['normal'] = nor
        self.fillColors['hover'] = hov

    def bntext(self,txt):
        self.buttonSurf = font.render(txt, True, (20, 20, 20))


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
        screen.blit(self.buttonSurface, self.buttonRect)

def myFunction():
    print('Button Pressed')

def myFunction1():
    aa = Bnd.objectsval
    print('Button --- Pressed' + str(aa))

customButton1 = Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
customButton2 = Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction1, 5)
customButton2.bncolor('#ff0000')
customButton2.bntext('hi')

# Game loop.
while True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for a in Bnd.objects:
        a.process()

    pygame.display.flip()
    fpsClock.tick(fps)


class VersionPF:
    number = '0.01'
    date = '21 Feb 265'
    text = 'start'
