class Marker:
    # __color = None
    # __name = None
    # __type = None
    # __brand = None
    # __price = None
    # __image = None

    def __init__(self,color,name,type,brand,price,image,):
        self.__color = color
        self.__name = name
        self.__type = type
        self.__brand = brand
        self.__price = price
        self.__image = image

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color

    def setName(self,name):
        self.__name = name
    
    def getName(self):
        return self.__name
    

object = Marker('red','monami','temporal','monami limited',56,'image.jpg',3)
# object.setColor('green')
# print(object.getColor())




object.setName('am')
print(object.getName())
