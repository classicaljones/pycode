# Database = [
#     {
#         'Student':'Giscard',
#         'id': 'y24se1703',
#         'programme':'software engineer',
#         'password': 123456
#     },
#     {
#         'Student':'Atta',
#         'id': 'y24se1704',
#         'programme':'software engineer',
#         'password': 1234567
#     },
#       {
#         'Student':'Jones',
#         'id': 'y24se1702',
#         'programme':'software engineer',
#         'password': 12345
#     },
#     {
#         'Student':'Michael',
#         'id': 'y24se1732',
#         'programme':'software engineer',
#         'password': 12345678
#     }
# ]

# def checker(student, password):
#     for data in Database:
#         if data['Student'] == student and data['password'] == password:
#             return True

# while True:
#     try:
#         student_name = str(input('Student name '))
#         student_password = int(input('Student password '))
#     except ValueError:
#         print('Check your inputs')
#     else:
#         break

# checks = checker(student_name, student_password)
# if checks:
#     print(f'Welcome {student_name}')
# else:
#     print('Wrong Credential')
for left in range(7):
    for right in range(left, 7):
        print(f'[{left}|{right}]', end='')
    print('\n')

