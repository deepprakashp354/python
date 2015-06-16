import pygame,sys
import pygame.mixer


pygame.init()
pygame.mixer.init() #Initialising the mixer


window=pygame.display.set_mode((300,200))

#name=pygame.font.SysFont("Courier",30)
#paintName=name.render("DB MALL",1,(255,0,0),(255,255,255))

paintName=pygame.image.load("mario.png") #loading image
paintName = pygame.transform.scale(paintName, (50, 50)) #setting size of the loaded image
myMusic=pygame.mixer.Sound("sound1.ogg") #Load sound


x,y=0,0
directionX,directionY=1,1
objectSize=paintName.get_size() #get_size() gives the width and height of the object and stores in a list objectSize
frameSpeed=pygame.time.Clock()  #a clock is initialized to control the timing of the object

while 1:
    frameSpeed.tick(50) #setting the timegap of the clock
    window.fill((255,255,255)) #filling the background with the black color

#  mouseCoordinates = pygame.mouse.get_pos() #gets the mouse position in the form of tuple
#  x=mouseCoordinates[0]
#  y=mouseCoordinates[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: #checks for if event is of keydown
            if event.key == pygame.K_LEFT: #checks which key has been pressed
                x-=5
            if event.key == pygame.K_RIGHT: #checks which key has been pressed
                x+=5
            if event.key == pygame.K_UP: #checks which key has been pressed
                y-=5
            if event.key == pygame.K_DOWN: #checks which key has been pressed
                y+=5

    if x < 0:
        x=1
        myMusic.stop() #stop the music
        myMusic.play() #plays the music
    if y < 0:
        y=1
        myMusic.stop() #stop the music
        myMusic.play() #plays the music
    if x + objectSize[0] > 300:
        x=300-objectSize[0]
        myMusic.stop() #stop the music
        myMusic.play() #plays the music
    if y + objectSize[1] > 200:
        y=200-objectSize[1]
        myMusic.stop()
        myMusic.play()

    window.blit(paintName,(x,y))

    pygame.display.update()