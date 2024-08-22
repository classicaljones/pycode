# php tutorial on crud
#
# age = 32
# name = 'jones'
# print(name + str(age))
#
# first_number = (input())
#
# second_number = (input())
#
# result = first_number + second_number
# print(result)  #
#
# age = int(input())
#
# if age < 18:
#     print('Can not vote')
# else:
#     print('You can vote')
#
# age = int(input('Your age '))
#
# first = int(input('First number '))
# second = int(input('second number '))
# third = int(input('third number '))
#
# if (first > second) and (first > third):
#     print('Fist number is the largest')
# elif (second > first) and (second > third):
#     print('Second number is the largest')
# elif (third > first) and (third > second):
#     print('Third number is the largest')
# else:
#     print('They are equal')
#
# first = int(input('First number '))
# second = int(input('second number '))
# third = int(input('third number '))
# fourth = int(input('Fourth number '))
#
# if first > second and first > third and first > fourth:
#     print('The first number is the largest')
# elif second > first and second > third and second > fourth:
#     print('The second number is the largest')
# elif third > second and third > first and third > fourth:
#     print("The third number is largest")
# elif fourth > second and fourth > third and fourth > first:
#     print("The fourth number is the largest")
# else:
#     print('They are all equal')
#
# if first > second and third and fourth:
#     print('first number is the largest')
# elif second > first and third and fourth:
#     print('second number is the largest')
# elif third > first and second and fourth:
#     print('third number is the largest')
# elif fourth > first and second and third:
#     print('fourth number is largest')
# else:
#     print('They are all equal')
#
# first = float(input('First number '))
# op = input('operation ')
# second = float(input('Second number '))
#
# if op == '*':
#     print(first * second)
# elif op == '+':
#     print(first + second)
# elif op == '/':
#     print(first / second)
# elif op == '-':
#     print(first - second)
# else:
#     print('Try again')
#
# check_number = int(input('Check '))
#
# if check_number % 2:
#     print('It is an odd number')
# else:
#     print('It is even number')
#
# name = 'kofi'
# print(name is 'k')
#
# list_of_numbers = (1, 2, 3, 4)
#
# print(list_of_numbers)
#
# def hello(to = 'hello'):
#     print(to)
#
# hello()

# score = int(input('Score '))
#
# if 90 <= score <= 100:
#     print('Grade: A')
# elif 80 <= score < 90:
#     print('Grade: B')
# elif 70 <= score < 80:
#     print('Grade: C')
# elif 60 <= score < 70:
#     print('Grade: D')
# else:
#     print('Grade: F')

# score = int(input('Number '))
#
# if score >= 90:
#     print('Grade: A')
# elif score >= 80:
#     print('Grade: B')
# elif score >= 70:
#     print('Grade: C')
# else:
#     print('Grade: F')
#
# if score % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# list1 = ['Giscard', 3, 'Michael', 'infinity']

# list2 = ['Jones', 9, 'Fordjour', 'infinity']

# compare = 'infinity' in list2

# if compare:
#     print('It is in')
# else:
#     print('It is not in')

# name = input('who? ')

# match name:
#     case 'Harry' | 'Fordjour' | 'Jones':
#         print('I know him')
#     case 'Justice' | 'Nti':
#         print('Dont remember ')
#     case _:
#         print('Dont get you')

# i = 3

# while i != 0:
#     print('meow')
#     i -= 1

# i = 0

# while i < 3:
#     print('hello')
#     i = i + 1

# for i in range(3):
#     print('hello')

# for _ in [1, 2, 4]:
#     print('hello')
# number = int(input('What is n '))

# while True:
#     if number > 2:
#         break


# for _ in range(number):
#     print('hello')

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What's n"))
#         if n > 0:
#             return n

# def meow(n):
#     for _ in range(n):
#         print('hello')


# for student in students:
#     print(student)
# To use string in range() we use len(x)
# students = ['Francis','Jones','Fordjour']

# for i in range(len(students)):
#     print(i + 1, students[i])

# Dictionary in python {'key': 'value'} pair

# students = {
#     'Jones': 'House 6',
#     'Michael': 'House 5',
#     'Fordjour': 'House 3',
#     'Gerald': 'House 1'
# }

# print(students['Jones'])
# print(students['Michael'])
# print(students['Gerald'])

# for student in students:
#     print(student, students[student], sep=", ")
#
# students = [
#     {'name': 'Jones', 'house': 'house 2', 'section': '3'},
#     {'name': 'Michael', 'house': 'house 4', 'section': '1'},
#     {'name': 'Fordjour', 'house': 'house 5', 'section': None}
# ]
#
# for student in students:
#     print(student['name'], student['house'])
#
# Engineer = []
# Engineer_1 = []
#
# if Engineer :
#     print('Loading...')
#     for list in Engineer:
#         print(list)
#     else:
#         print('No record found')

def main(size):
    print_square(size)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()


main(3)
