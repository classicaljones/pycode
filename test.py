# number = int(input('Number '))
#
# divisible = (number % 23 == 0)
#
# if divisible:
#     print('It is divisible by 23')
# else:
#     print('Not divisible by 23')

# number = int(input('Number '))
#
# last_number = number % 10
#
#
# if last_number % 23 == 0:
#     print('It is divisible')
# else:
#     print('Not divisible')

# number = int(input('Check if it is multiple of 50 '))

# factors_of_50 = (50 % number == 0)

# if factors_of_50:
#     print('It is a multiple of 50')
# else:
#     print('Not a multiple of 50')


# number_of_people = int(input('number of people in the room '))
#
# if number_of_people == 4:
#     print('Bright by 4x')
# elif number_of_people == 3:
#     print('Bright by 3x')
# elif number_of_people == 2:
#     print('Bright by 2x')
# elif number_of_people == 1:
#     print('Bright by 1x')
# elif number_of_people == 0:
#     print('Light off')

# personnel_one = input('Personnel One ')
# personnel_two = input('Personnel Two ')
#
# if personnel_one == 'president' and personnel_two == 'vice president':
#     print('safe open')
# elif personnel_one == 'president' and personnel_two == 'speaker':
#     print('safe open')
# elif personnel_one == 'vice president' and personnel_two == 'speaker':
#     print('safe open')
# else:
#     print('safe lock')


# names = ['Giscard', 'Jones', 'Atta Kay']
#
# for i in names:
#     print(i)

# Set = {'Giscard', 'Jones', 'Atta', 122}

# while True:
#     number_present = int(input('Number of people present '))

#     if number_present >= 3:
#         print('The light is bright')
#     elif number_present == 2:
#         print('The light is Dim')
#     elif number_present == 1:
#         print('The light is Dimmer')
#     else:
#         print('The light is off')
#         print('Sleep mode...')
#     print('Still detecting')

# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

# response = requests.get('http://itunes.apple.com/search?entity=song&limit&term' + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

# class MyClass:
#     var1 = 2
#     def func(self,x):
#         return self.var1 + x0
    
# mc = MyClass()

# print(mc.var1)

# github/mrbbasx

# from say import square
# import sys

# def main():
#     test_square()

# def test_square():
#     assert square(2) == 4
#     assert square(5) == 25

# if __name__ == '__main__':
#     main()

# class Personal_Information:
#     age = None
#     first_name: None

#     def __init__(self,firstName,Surname,MiddleName):
#         self.first_name = firstName
#         self.surname = Surname
#         self.middle_name = MiddleName

# object = Personal_Information()
# print(object.age)

# class Legible_voters:

#     def ageFxn(age):
#         return age >= 18


# voters_age = int(input('What is your age '))

# object = Legible_voters

# if object.ageFxn((voters_age)):
#     print('You can vote')
# else:
#     print('Cannot vote')


# class Cal_Shape:

#     def triangle(length,height, width):
#         volume = 0.5 * (length * height * width)
#         return volume
    
#     def square(length):
#         area = (length ** 2)
#         return area
    
#     def cube(length):
#         volume = (length ** 3)
#         return volume

# object_shape = Cal_Shape

# print(object_shape.square(2))
# print(object_shape.triangle(2,3,2))
# print(object_shape.cube(2))

Database = [
    {
        'Student':'Giscard',
        'id': 'y24se1703',
        'programme':'software engineer',
        'password': 123456
    },
    {
        'Student':'Atta',
        'id': 'y24se1704',
        'programme':'software engineer',
        'password': 1234567
    },
      {
        'Student':'Jones',
        'id': 'y24se1702',
        'programme':'software engineer',
        'password': 12345
    },
    {
        'Student':'Michael',
        'id': 'y24se1732',
        'programme':'software engineer',
        'password': 12345678
    }
]


class Databases:
    student = None
    id = None
    programme = None
    password = None

    def __init__(self,Student,Id,Programme,Password):
        self.student = Student
        self.id = Id
        self.programme = Programme
        self.password = Password

    def getStudent():
        

object = Database()


