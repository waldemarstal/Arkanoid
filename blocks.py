import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((23, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.kill2 = False
        self.next = 0
        self.life = 1
    def boom(self):
        self.life -= 1
        if self.life == 2:
            self.image.fill((255,255,255))
        elif self.life == 1:
            self.image.fill((128,128,128))
        elif self.life == 0:
            self.kill2 = True
    def update(self):
        if (self.kill2==True) and (self.next<=6):
            self.next += 1
            if self.next % 2 == 0:
                self.image.fill((150,150,150))
            else:
                self.image.fill((0,0,0))
        if self.next == 6:
            self.kill()