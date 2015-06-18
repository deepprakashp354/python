class GameObject:
    def __init__(self,position ,size ,image):
        self.__position = position  #making the private('__') variable visible globally in the class
        self.__size = size          #              ||
        self.__image = image        #              ||

    def getPosition(self):        #making the private variables of the class available to other classes if requested
        return self.__position

    def setPosition(self, position): #setting the private variables of the class from other classes if requested
        self.__position=position

    def getSize(self):        #making the private variables of the class available to other classes if requested
        return self.__size

    def setSize(self, size): #setting the private variables of the class from other classes if requested
        self.__size=size

    def getImage(self):        #making the private variables of the class available to other classes if requested
        return self.__image

    def setImage(self, image): #setting the private variables of the class from other classes if requested
        self.__image=image

    def intersects(self,other):
        pass