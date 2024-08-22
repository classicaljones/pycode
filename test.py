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

number = int(input('Number '))

factors_of_50 = (50 % number == 0)

if factors_of_50:
    print('It is a multiple of 50')
else:
    print('Not multiple of 50')