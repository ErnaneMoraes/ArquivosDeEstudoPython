from random import randint

num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(num)

print(f'O maior valor foi: {max(num)}')
print(f'O menor valor foi: {min(num)}')
