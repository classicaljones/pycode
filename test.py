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

personnel_one = input('Personnel One ').strip()
personnel_two = input('Personnel Two ').strip()
p = 'president'
vp = 'vice president'
sp = 'speaker'

if personnel_one == p and personnel_two == vp:
    print('safe open')
elif personnel_one == p and personnel_two == sp:
    print('safe open')
elif personnel_one == vp and personnel_two == sp:
    print('safe open')
else:
    print('safe lock')
