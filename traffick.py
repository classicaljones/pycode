class Traffick:
    def __init__(self) -> None:
        self.__red = 'Red'
        self.__green = 'Green'
        self.__yellow = 'Yellow'

    def time(self):
        return '60000 ms'
    
    # def traffickLight(self):
    #     print(f'{self.__red} wait {self.time()}')
    #     print(f'{self.__yellow} wait {self.time()}')
    #     print(f'{self.__green} wait {self.time()}')
      
    def red(self):
        return self.__red
    
    def yellow(self):
        return self.__yellow
    
    def green(self):
        return self.__green 

    

