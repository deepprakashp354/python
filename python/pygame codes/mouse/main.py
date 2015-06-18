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
    window.fill((255,255,255)) #filling the background with the black color

    mouseCoordinates = pygame.mouse.get_pos() #gets the mouse position in the form of tuple
    x=mouseCoordinates[0]
    y=mouseCoordinates[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if x + objectSize[0] > 500:
        x= 500 - objectSize[0]
    if y + objectSize[1] > 400:
        y= 400 - objectSize[1]

    window.blit(paintName,(x,y))

    pygame.display.update()