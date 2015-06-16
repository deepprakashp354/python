import pygame,sys

pygame.init()

size=(600,660)
l=0
m=0
window=pygame.display.set_mode(size)

font1=pygame.font.SysFont("Courier",30)
text=font1.render("Deep",1,(255,255,255),(0,0,255))

directionX=0
boardSize=text.get_size()
framespeed=pygame.time.Clock()

while 1:
    framespeed.tick(10)
    for x in pygame.event.get():
        print(x)

        if x.type==pygame.QUIT:
            sys.exit()

    window.blit(text,(l,m))

    l=l+ 5*directionX
    if l+boardSize[0] > 500 or l<=0:
        directionX *= -1
    l=l+20
    pygame.display.update()