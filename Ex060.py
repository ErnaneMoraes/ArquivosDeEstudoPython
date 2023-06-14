n1 = int(input(f'Digite um numero: '))
i = n1
fat = 1
while i > 0:
    print(f'{i}', end=(' '))
    if i > 1:
        print(f' x ', end=(' '))
    else:
        print(f' = ', end=(' '))
    fat *= i
    i -= 1

print(f'{fat}', end=(' '))

