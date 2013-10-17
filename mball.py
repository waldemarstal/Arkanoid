import pygame
from pygame.locals import *
import math
class Ball(pygame.sprite.Sprite):
    x = 0.0
    y = 180.0
    direction = 200
    width=10
    height=10
    def __init__(self):
        self.speed = 10.0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('kulka.png')
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.life = 4
    def bounce(self,diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff
    def update(self):
        direction_radians = math.radians(self.direction)
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
        self.rect.x = self.x
        self.rect.y = self.y
        if self.y <= 0:
            self.bounce(0)
            self.y=1
        if self.x <= 0:
            self.direction = (360-self.direction)%360
            self.x=1
        if self.x > self.screenwidth-self.width:
            self.direction = (360-self.direction)%360
            self.x=self.screenwidth-self.width-1
        if self.y > 600:
            self.life -= 1
            self.y = 200
            self.x = 0
            self.direction = 200