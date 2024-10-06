class Animal:
    def __init__(self) -> None:
        self.n = 'animal sound'

    def getSound(self):
        return self.n
    
    def setSound(self,n):
        self.n = n