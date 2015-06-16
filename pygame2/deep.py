import pygame,sys
from math import *

pygame.init()

windowSize=(600,600)
window=pygame.display.set_mode(windowSize)

x,y=0,0

pygame.image.load("mario.jpg")
#font1=pygame.font.SysFont("Courier",50)
#dot=font1.render(".",1,(0,0,0),(255,255,255))

frameSize=pygame.time.Clock()

while 1:
    frameSize.tick(30)
    y=y+10
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        window.blit(dot,(x,y))

    pygame.display.update()