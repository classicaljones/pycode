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

def main():
    x = int(input("What`s x "))
    print(f"x square is {square(x)}")


def square(n):
    return n * n


if __name__ == "__main__":
    main()
