#Write down the changes with the date:
#04012015 - 1. Dude cannot move out of boundaries 
#           2. Wall boundaries created
#who is next?

import pygame, sys, random, math
from pygame.locals import *

FPS = 30

DUDESPD = 5 

#COLOR
YELLOW = (100, 50, 0)
BGCOLOR = (255, 255, 255) #WHITE
BLUE = (0, 255, 255)
BLACK = (0, 0, 0)

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
WINDOWBORDER = 20

def main():
	global DISPLAYSURF, FPSCLOCK

	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
	pygame.display.set_caption('rpg')

	DISPLAYSURF.fill(BGCOLOR)
	while True: 
		runGame()

def runGame(): 
	x = WINDOWWIDTH / 2
	y = WINDOWHEIGHT / 2 
	dudePosition = [x, y]
	bulletPosition = [0, 0]
	bulletShow = False
	bulletTic = 0 

	moveRight = False
	moveLeft = False
	moveUp = False
	moveDown = False 

	pygame.mouse.set_visible(False)
	while True: #Game loop
		for event in pygame.event.get(): # event handling loop
	  		if event.type == QUIT:
	  			terminate()
	  		if event.type == KEYDOWN:
	  			if ((event.key == K_LEFT or event.key == K_a) and dudePosition[0] >= WINDOWBORDER):
	  				dudePosition[0] -= DUDESPD
	  				moveLeft = True
	  			if ((event.key == K_RIGHT or event.key == K_d) and dudePosition[0] <= WINDOWWIDTH - WINDOWBORDER):
	  				dudePosition[0] += DUDESPD
	  				moveRight = True
	  			if ((event.key == K_UP or event.key == K_w) and dudePosition[1] >= WINDOWBORDER):
		  			dudePosition[1] -= DUDESPD 
	  				moveUp = True
	  			if ((event.key == K_DOWN or event.key == K_s) and dudePosition[1] <= WINDOWHEIGHT - WINDOWBORDER): 
	  				dudePosition[1] += DUDESPD 
	  				moveDown = True
	  			if event.key == K_ESCAPE:
		  			terminate()
	  		if event.type == KEYUP:
	  			if(event.key == K_LEFT or event.key == K_a and dudePosition[0] >= WINDOWBORDER):
	  				moveLeft = False
	  			if(event.key == K_RIGHT or event.key == K_d and dudePosition[0] <= WINDOWWIDTH - WINDOWBORDER):
	  				moveRight = False
	  			if (event.key == K_UP or event.key == K_w and dudePosition[1] >= WINDOWBORDER):
	  				moveUp = False
	  			if (event.key == K_DOWN or event.key == K_s and dudePosition[1] <= WINDOWHEIGHT - WINDOWBORDER):
	  				moveDown = False
	  		if event.type == MOUSEBUTTONUP:
	  			bulletPosition = pygame.mouse.get_pos()
	  			print bulletPosition 
	  			bulletShow = True

	  	#key held down 
	  	if moveLeft and dudePosition[0] >= WINDOWBORDER: 
	  		dudePosition[0] -= DUDESPD
	  	if moveRight and dudePosition[0] <= WINDOWWIDTH - WINDOWBORDER:
	  		dudePosition[0] += DUDESPD 
	  	if moveUp and dudePosition[1] >= WINDOWBORDER:
	  		dudePosition[1] -= DUDESPD
	  	if moveDown and dudePosition[1] <= WINDOWHEIGHT - WINDOWBORDER:
	  		dudePosition[1] += DUDESPD 

	 

		DISPLAYSURF.fill(BGCOLOR)
		for yCoor in range(0, 480):
			WallPosition = [0, yCoor]
			drawWall(WallPosition)
		for yCoor in range(0, 480):
			WallPosition = [640, yCoor]
			drawWall(WallPosition)
		for xCoor in range(0, 640):
			WallPosition = [xCoor, 0]
			drawWall(WallPosition)
		for xCoor in range(0, 640):
			WallPosition = [xCoor, 480]
			drawWall(WallPosition)
		

		if bulletShow:
	  		drawBullet(dudePosition, bulletPosition)
	  		bulletTic = bulletTic + 1
	  		if bulletTic == 3:
	  			bulletShow = False
	  			bulletTic = 0

		drawDude(dudePosition)
		drawCrossHair()
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def drawDude(pos): 
	pygame.draw.circle(DISPLAYSURF, YELLOW, pos, 5)

def drawCrossHair():
	mousePos = pygame.mouse.get_pos()
	crossBox = pygame.Rect(mousePos[0], mousePos[1], 5, 5)
	pygame.draw.rect(DISPLAYSURF, YELLOW, crossBox)

def drawBullet(dudePos, bulletPos):
	print dudePos, bulletPos
	pygame.draw.line(DISPLAYSURF, YELLOW, dudePos, bulletPos, 2)

def drawWall(pos):
	pygame.draw.circle(DISPLAYSURF, BLACK, pos, 10)


if __name__ == '__main__':
	main()