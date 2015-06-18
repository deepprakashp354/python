__author__ = 'Deep Prakash'
class collision:
    def __init__(self,x,y,width,height):
        self.x=x  #self.__x=x means x belongs to only this class, it is not visible to the outer world
        self.y=y  #__y , means it is a private attribute
        self.width=width
        self.height=height

    def setPosition(self,x,y): #setPosition of the object
        self.x=x
        self.y=y

    def __intersectsX(self,other): #checking for the conditions of x axis and returning true or false accordingly
        k=self.width/2
        if self.x >= other.x and self.x <= (other.x + other.width + k) :  #other is an object passed to this method
            return 1
        if (self.x + self.width + k) >= other.x and (self.x + self.width + k) <= (other.x + other.width):
            return 1
        return 0

    def __intersectsY(self,other): #checking for the conditions of y axis and returning true or false accordingly
        l=self.height/2
        if self.y >= other.y and self.y <= (other.y + other.height + l) :  #other is an object passed to this method
            return 1
        if (self.y + self.height + l) >= other.y and (self.y + self.height + l) <= (other.y + other.height + l):
            return 1
        return 0

    def intersect(self,other): #providing the intersectsx and intersectsy with the object and checking what it returns
        if self.__intersectsX(other) and self.__intersectsY(other):
            return 1
        return 0