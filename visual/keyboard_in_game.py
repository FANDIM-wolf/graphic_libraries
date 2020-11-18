#driver for keyboard and 
#  also it  tracks user's buttons

import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

x,y= 0,0

move_x , move_y = 0,0

while True :
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
		#we pressed button	
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				move_x = -1
			elif event.key == K_RIGHT:
				move_x = +1
			elif event.key == K_UP:
				move_x = -1
			elif event.key == K_DOWN:
				move_x = +1
		elif event.type == KEYUP:
			if event.key == K_LEFT:
				move_x = 0 
			elif event.key == K_RIGHT:
				move_x = 0 
			elif event.key == K_UP:
				move_y = 0
			elif event.key == K_DOWN:
				move_y = 0
		x+= move_x 
		y+= move_y
		screen.fill((0,0,0))
		pygame.display.update()		 
				

        #x+= move_x
        #y+= move_y

        #screen.fill((0,0,0)) // color of background 

        #pygame.display.update()
