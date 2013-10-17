import pygame
from pygame.locals import *
class Bonus(pygame.sprite.Sprite):
    def __init__(self,ob,pos):
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = pos
        self.img = ob
        self.image = pygame.image.load(self.img)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.dy = 3
    def update(self):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.y += self.dy 
        if self.y > 600:
            self.kill()
    def boom(self):
        self.kill()
    def draw(self, screen):
        screen.blit(self.image, (self.rect.left,self.rect.top) )        