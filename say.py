# users = {'Hans' : 'active', 'Elenoe': 'inactive', '???': 'active'}

# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#         print(active_users)

# for n in range(2, 50):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime number')
        
# for n in range(2, 30):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equal', x, '*', n//x)
#             break
#     else:
#         print(n, 'is a prime a number')

# def recursive_binary_search(list, target):
#     if len(list) == 0:
#         return False
#     else:
#         midpoint = (len(list)) // 2

#         if list[midpoint] == target:
#             return True
#         else:
#             if list[midpoint] < target:
#                 return recursive_binary_search(list[midpoint+1:],target)
#             else:
#                 return recursive_binary_search(list[:midpoint],target)
# def verify(result):
#     print('Target found: ', result)

# number = [1, 2, 3, 4, 5, 6, 7, 8]
# result = recursive_binary_search(number, 12)
# verify(result)

# result = recursive_binary_search(number, 6)
# verify(result)

# def main():
#     hello('world')
#     goodbye('world')

# def hello(name):
#     print(f'hello, {name}')

# def goodbye(name):
#     print(f'goodbye {name}')

# if __name__ == '__main__':
#     main()

def main():
    x = int(input('Square number '))
    print(square(x))

def square(number):
    return (number * number)


if __name__ == '__main__':
    main()