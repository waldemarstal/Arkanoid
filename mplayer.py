import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width=75
        self.height=15
        self.im = 'deska.png'
        self.image = pygame.image.load(self.im)
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.topleft = (0,self.screenheight-self.height)
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.left = pos[0]
        if self.rect.left > self.screenwidth - self.width:
            self.rect.left = self.screenwidth - self.width
    def zm(self):
        self.im = 'deska2.png'
        self.width = 125
        self.image = pygame.image.load(self.im)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,self.screenheight-self.height)
    def zm2(self):
        self.im = 'deska.png'
        self.width == 75
        self.image = pygame.image.load(self.im)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,self.screenheight-self.height)