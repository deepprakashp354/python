import pygame
import sys

pygame.init()

windowSize=(600,450)                         #simply a tuple
window = pygame.display.set_mode(windowSize) #to show a window having the window's size equal to windowSize tuple value, and store what is being returned in the variable named window

name=pygame.font.SysFont("Courier",25)       #creating the font for the text

text=name.render("Deep Prakash, will let you fall",1,(255,0,255),(255,255,255)) #paints the string with font defined in the name by pygame.font.sysFont()
                                                                       #1 here after the comma is the opacity of the string.
                                                                       #

while 1:
    for x in pygame.event.get():  #mouse event, .get() gets all the event
      if x.type == pygame.QUIT:   #if the event captured by pygame.event matches pygame.QUIT: sys.exit(), it closes the window
        sys.exit()                #sys.exit() is an window event that occurs when the mouse is clicked on cross button

    window.blit(text,(0,0))       #adding the string to the event at o,o position
    pygame.display.update()
