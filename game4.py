#!/usr/bin/python
import pygame
import time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
done = False

#setting
FPS = 60

#warna
coklat = (212, 161, 144)
red = (255, 0, 0)
biru = (0, 0, 255)
hitam = (0, 0, 0)
birucair = (0, 248, 252)

#fps
clock = pygame.time.Clock()



#img
#img = pygame.image.load('awan.png')

#asalkodinat

#x=polis,x1=pencuri
x = 700
y = 100
x1 = 10
y1 = 100
nyawa1 = 100
tenaga = 100
pkalah = 0
pskalah = 0

#text
myfont = pygame.font.SysFont(None, 30)

text = myfont.render('POLIS ENTRI', True, biru)
text2 = myfont.render('BIRU KEJAR MERAH', True, biru)
#nyawa_pencuri = myfont.render(str(nyawa1), True, biru)
#screen.blit(text, (100, 100))
#pygame.display.update()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	#text
	screen.blit(text, (350, 1))#tajuk
	screen.blit(text2, (310, 20))#tajuk
	nyawa_pencuri = myfont.render(str(nyawa1), True, biru)#nilai nyawa pencuri
	screen.blit(nyawa_pencuri, (1, 1))#nilai nyawa pencuri
	
	tenaga_polis = myfont.render(str(tenaga), True, biru)#nilai nyawa pencuri
	screen.blit(tenaga_polis, (750, 1))#nilai nyawa pencuri


	#butang
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: 
		y -= 3
		tenaga -= 0.05
	if pressed[pygame.K_DOWN]: 
		y += 3
		tenaga -= 0.05
	if pressed[pygame.K_LEFT]: 
		x -= 3
		tenaga -= 0.05
	if pressed[pygame.K_RIGHT]: 
		x += 3
		tenaga -= 0.05

	if pressed[pygame.K_w]: y1 -= 3
	if pressed[pygame.K_s]: y1 += 3
	if pressed[pygame.K_a]: x1 -= 3
	if pressed[pygame.K_d]: x1 += 3

	pygame.display.update()
	screen.fill((199, 199, 199))
	
	#kotak
	pygame.draw.rect(screen, hitam, pygame.Rect(40, 10, 300, 10))#nyawa pencuri back
	pygame.draw.rect(screen, hitam, pygame.Rect(490, 10, 250, 10))#tenaga polis back
	pygame.draw.rect(screen, biru, pygame.Rect(x, y, 60, 60))#polis
	pygame.draw.rect(screen, red, pygame.Rect(x1, y1, 60, 60))#pencuri
	pygame.draw.rect(screen, red, pygame.Rect(40, 10, nyawa1*3, 10))#nyawa pencuri
	pygame.draw.rect(screen, biru, pygame.Rect(490, 10, tenaga*2.5, 10))#tenaga polis

	#kotak air
	pygame.draw.rect(screen, birucair, pygame.Rect(500, 500, 10, 10))#kotak air
	pygame.draw.rect(screen, birucair, pygame.Rect(250, 410, 10, 10))#kotak air
	

	#persentuhan dua kotak
	if (x >= x1 and x <= x1+60 and y >= y1 and y <= y1+60) or (x+60 >= x1 and x+60 <= x1+60 and y+60 >= y1 and y+60 <= y1+60):
		nyawa1 -= 1		

	#tambah tenaga
	if (x >= 500 and x <= 510 and y >= 500 and y <= 510) or (x >= 250 and x <= 260 and y >= 410 and y <= 420):
		tenaga += 5
	#tambah nyawa
	if (x1 >= 500 and x1 <= 510 and y1 >= 500 and y1 <= 510) or (x1 >= 250 and x1 <= 260 and y1 >= 410 and y1 <= 420):
		nyawa1 += 5
	
	#over error
	if nyawa1 > 100 :
		nyawa1 = 100
		
	if tenaga > 100 :
		tenaga = 100
		

	#zero error
	if nyawa1 < 0 :
		nyawa1 = 0
		pkalah = 1
	if tenaga < 0 :
		tenaga = 0
		pskalah = 1
	
	#pencuri kalah		
	if pkalah == 1 :
		pen_kalah = myfont.render("pencuri kalah", True, red)
		screen.blit(pen_kalah, (300, 300))
	#polis kalah		
	if pskalah == 1 :
		polis_kalah = myfont.render("polis kalah", True, red)
		screen.blit(polis_kalah, (300, 300))

	#img
	#screen.blit(img, (0,120))
	#pygame.display.flip()
	
	#fps
	clock.tick(FPS)

pygame.quit()
