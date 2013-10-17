from mplayer import Player
from bonusy import Bonus
from blocks import Block
from mball import Ball
from random import randint
import math
import pygame
from pygame.locals import *
from sys import exit 
czas = 0
wynik = 10
pygame.init()
font1 = pygame.font.SysFont("CatShop.ttf",30)
font2 = pygame.font.Font("CatShop.ttf", 72)
screengl = pygame.display.set_mode([800, 600])
screen = pygame.image.load('tlo.jpg')
pygame.display.set_caption('Arkanoid')
pygame.mouse.set_visible(0)
pygame.mixer.init()
sound = pygame.mixer.Sound("sound.wav")
e_sound = pygame.mixer.Sound("error.wav")
w_sound = pygame.mixer.Sound("w.wav")
nl_sound = pygame.mixer.Sound("nl.wav")
go = pygame.mixer.Sound("GAME OVER YEAH.wav")
gameover = pygame.Surface((800,600))
gameover.fill((250,250,250))
pygame.time.set_timer(USEREVENT, 3000)
font = pygame.font.Font(None, 36)
blocks=pygame.sprite.RenderPlain()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.RenderPlain()
player = Player()
allsprites.add(player)
ball = Ball()
allsprites.add(ball)
balls.add(ball)
dod = pygame.sprite.Group()
lev = 1
g = 0
k = open('k.txt').read()
exec(k)
pygame.time.set_timer(USEREVENT, 3000)	    
clock = pygame.time.Clock()
exit_program = False
lll = ball.life
while exit_program != True:
    clock.tick(30)
    screen = pygame.image.load('tlo.jpg')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        if event.type == KEYDOWN:
	    if event.key == K_f:
		screen = pygame.display.set_mode((800,600),FULLSCREEN,32)
	if event.type == KEYDOWN:
	    if event.key == K_n:
		screen = pygame.display.set_mode((800,600),32)
	if event.type == KEYDOWN:
	    if event.key == K_k:
		blocks.empty()
	if event.type == USEREVENT:
            wynik -= 1 * lev
    if ball.life == 0:
        gameover.fill((250,250,250))
	tekst2 = font2.render("GAME OVER", True, (0,0,0) )          
	gameover.blit( tekst2, (170,200) )
	screengl.blit(gameover, (0,0))
	g += 1
	if g < 210:
	   go.play()
	else:
	    exit_program = True
	pygame.display.update()
    else:
	if len(dod) > 0:
	    for d in dod:
		if pygame.sprite.collide_rect(d,player):
		    d.boom()
		    if d.img == 'serce.png':
			if ball.life <= 7:
			    ball.life += 1		    
		    elif d.img == 'fast.png':
			if ball.speed <= 20:
			    ball.speed += 2
		    elif d.img == 'slow.png':
			if ball.speed > 8:
			    ball.speed -= 2
		    elif d.img == 'slim.png':
			player.zm2()
			player.update()
		    elif d.img == 'fat.png':
			player.zm()
			player.update()
		    elif d.img == 'pkt.png':
			wynik += 50
		    elif d.img == 'pktmin.png':
			wynik -= 30
	if pygame.sprite.spritecollide(player, balls, False):
	    diff = (player.rect.left + player.width/2) - (ball.rect.left+ball.width/2)
	    ball.rect.top = screen.get_height() - player.rect.height - ball.rect.height -1
	    ball.bounce(diff)
	deadblocks = pygame.sprite.spritecollide(ball, blocks, False)
	if len(deadblocks) > 0:
	    ball.bounce(0)
	    ball.update()
	    sound.play()
	    wynik += 10 * lev
	    for b in deadblocks:
                b.boom()
		pos = b.x + 12, b.y
		a = randint(0,12 * lev)
		if a == 10:
		    cos = Bonus('serce.png', pos)
		    dod.add(cos)
		if a == 8:
		    cos = Bonus('fast.png', pos)
		    dod.add(cos)
		if a == 6:
		    cos = Bonus('slow.png', pos)
		    dod.add(cos)
		if a == 4:
		    cos = Bonus('slim.png', pos)
		    dod.add(cos)
		if a == 2:
		    cos = Bonus('fat.png', pos)
		    dod.add(cos)
		if a == 0:
		    cos = Bonus('pkt.png', pos)
		    dod.add(cos)
		if a == 12:
		    cos = Bonus('pktmin.png', pos)
		    dod.add(cos)
	if len(blocks) == 0:
	    lev += 1
	    dod.empty()
	    nextlev = 0
	    if lev == 4:
		while True:
		   gameover.fill((250,250,250))
		   tekst5 = font2.render("VICTORY!", True, (0,0,0) )
		   gameover.blit( tekst5, (180,150) )
		   tekst6 = font1.render("SCORE: " + str(wynik), True, (0,0,0) )
		   gameover.blit( tekst6, (320,250) )
		   screengl.blit(gameover, (0,0))
		   if lev < 1000:
		      lev += 1
		      w_sound.play()
		   pygame.display.update()
	    blocks.empty()
	    while nextlev < 600:
		nextlev += 1
		gameover.fill((250,250,250))
		tekst2 = font2.render("  LEVEL " + str(lev), True, (0,0,0) )          
		gameover.blit( tekst2, (180,150) )
		screengl.blit(gameover, (0,0))
		nl_sound.play()
		pygame.display.update()
	    if lev == 2:
		    for i in range(4):
			    for column in range(32):
				if i % 2 == 1:
					if column % 2 == 1:
						block=Block((100,100+20*i,250-30*i),column*(25)+1,120+i*20)
						block.life = 2
						blocks.add(block)
				else:
					if column % 2 == 0:
						block=Block((100,100+20*i,250-30*i),column*(25)+1,120+i*20)
						block.life = 2
						blocks.add(block)
	    if lev == 3:
		    for i in range(5):
			for column in range(32):
				if column % 2 == 0:
				    block=Block((40*i,250-50*i,60*i),column*(25)+1,120+i*23)
				    block.life = 3
				    blocks.add(block)
	    ball.y = 220
            ball.x = 0
            ball.direction = 200
	allsprites.draw(screen)
	blocks.draw(screen)
	dod.draw(screen)
	tekst = font1.render(str(czas+((pygame.time.get_ticks())/1000)), True, (255,0,0) )
	tekst1 = font1.render(str(wynik), True, (255,0,0) )          
	for i in range(ball.life):
            serce = pygame.image.load('serce.png')
            screen.blit(serce, ((i*25)+606, 15)) 
	screen.blit( tekst, (172,15) )
	screen.blit( tekst1, (400,13) )
	player.update()
	ball.update()
	if lll != ball.life:
	    if lll > ball.life:    
		player.zm2()
		player.update()
		e_sound.play()
	    lll = ball.life
	dod.update()
	blocks.update()
	screengl.blit(screen, (0,0))
	pygame.display.update()
pygame.quit()