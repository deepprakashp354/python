import pygame,sys

pygame.init()

size=(1200,660)
l=0
m=0
window=pygame.display.set_mode((l,m))

font1=pygame.font.SysFont("Courier",30)
text=font1.render(".",1,(255,255,255))

framespeed=pygame.time.Clock()

while 1:
    framespeed.tick(5)
    for x in pygame.event.get():
        print(x)

        if x.type==pygame.QUIT:
            sys.exit()

    l=l+20
    if(l<800 and l>0):
        window.blit(text,(l,m))
    else:
        l=l-20
        window.blit(text,(l,m))
        m=m+20

    pygame.display.update()