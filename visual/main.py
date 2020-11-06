import pygame
from  pygame.locals import *
from  sys import  exit
background_image_filename ="logo.png"
mouse_stripe = "mouse_stripe.png"
#base code
pygame.init()

#size of window
screen=pygame.display.set_mode((640,480),0,32)
#caption of window
pygame.display.set_caption("Action Journery")

mouse_cursor=pygame.image.load(mouse_stripe).convert_alpha()
image=pygame.image.load(background_image_filename).convert()

while True:
    for event in pygame.event.get():
        #if we wanna leave game
        if event.type == QUIT:
            pygame.quit()
            exit()
        #show stripe in our image 
        screen.blit(image,(0,0))
        x,y =pygame.mouse.get_pos()
        x-= mouse_cursor.get_width()/2
        y-=mouse_cursor.get_height()/2
        screen.blit(mouse_cursor,(x,y))
        pygame.display.update()