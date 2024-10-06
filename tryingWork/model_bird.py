class Bird:
    Right_wing = None
    Left_wing = None
    Right_leg = None
    Left_leg = None
    def __init__(self):
        ...

    def wing(self,Left_wing,Right_wing ):
        if (self.Left_wing == True or self.Right_wing == True):
            return 'The wings are flapping and Ready to fly'
        else:
            return 'The right wing or left wing is off. Not flying'
    


objBird = Bird()

print(objBird.wing(False,False))