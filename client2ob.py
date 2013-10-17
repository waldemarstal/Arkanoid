#!/usr/bin/env python 
import pygame
from pygame.locals import *
from sys import exit

class dod(pygame.sprite.Sprite):
  def __init__(self, pos,img):
    pygame.sprite.Sprite.__init__(self)
    self.x, self.y = pos
    self.img = img
    self.image = pygame.image.load(self.img).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.centerx = self.x
    self.rect.centery = self.y
  def update(self):
    self.rect.centerx = self.x
    self.rect.centery = self.y
  def draw(self, screen):
    screen.blit(self.image, (self.rect.left,self.rect.top) ) 