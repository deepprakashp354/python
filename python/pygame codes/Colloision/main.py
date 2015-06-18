__author__ = 'Deep Prakash'


import sys
import pygame
from collision import collision         #it is important that if we import our class file, we first create a __init__.py file, it acts like an intermediate
                                        # the first collision being imported is the filename here and the another collision is the class name

pygame.init()
pygame.mixer.init()

windowSize=(800,700)

screen=pygame.display.set_mode(windowSize)

#Adding Resources
otherObject=pygame.image.load("mario.png")
sound=pygame.mixer.Sound("sound1.ogg")

collisionText= pygame.font.SysFont("Courier",28)
renderText=collisionText.render("Hey i am Intersected", 1,(255,255,0),(0,0,0))

otherObjectSize=otherObject.get_size()
otherObject.fill((255,255,255),None, pygame.BLEND_RGBA_MAX)


x,y=0,0

clock=pygame.time.Clock()
directionX,directionY=1,1

def playSound():
    sound.stop()
    sound.play()

rectangle = collision(0,0,400,400)#New object square
mario = collision(0,0,otherObjectSize[0],otherObjectSize[1]) #new object, the otherObject

while 1:
    clock.tick(30)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    captureMouse = pygame.mouse.get_pos()
    x = captureMouse[0]
    y = captureMouse[1]

    mario.setPosition(x,y)

    if mario.intersect(rectangle):
        screen.blit(renderText,(10,10))
        playSound()

    pygame.draw.rect(screen,(255,255,255),(100,100,400,400),1)
    screen.blit(otherObject,(x,y))

    pygame.display.update()