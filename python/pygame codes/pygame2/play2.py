import pygame,sys

pygame.init()

window=pygame.display.set_mode((500,400))

name=pygame.font.SysFont("Courier",30)
paintName=name.render("DB MALL",1,(255,0,0),(255,255,255))

x,y=0,0
directionX,directionY=1,1
objectSize=paintName.get_size() #get_size() gives the width and height of the object and stores in a list objectSize
frameSpeed=pygame.time.Clock()  #a clock is initialized to control the timing of the object

while 1:
    frameSpeed.tick(50) #setting the timegap of the clock
    window.fill((0,0,0)) #filling the background with the black color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    window.blit(paintName,(x,y))

    x = x + 5*directionX
    y = y + directionY

    if x+objectSize[0] > 500 or x<=0:
        directionX *= -1
    if y + objectSize[1] > 400 or y<=0:
        directionY *=-1

    pygame.display.update()