import pygame


keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0,
           "num0": pygame.K_KP0,
           "num1": pygame.K_KP1,
           "num2": pygame.K_KP2,
           "num3": pygame.K_KP3,
           "num4": pygame.K_KP4,
           "num5": pygame.K_KP5,
           "num6": pygame.K_KP6,
           "num7": pygame.K_KP7,
           "num8": pygame.K_KP8,
           "num9": pygame.K_KP9}

class Background:
    def __init__(self,screen_in, area):  # even no.
        self.screen = screen_in

        self.area = area  #(0, 0, 800, 800)

        self.stagePosX = 0
        self.stagePosY = 0

        # self.screen.blit(self.bkground, [0, 0])
        #self.surface = screen.copy()

    def center(self,x,y):



        pass

