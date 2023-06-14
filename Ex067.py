while True:
    num = int(input(f'Digite um numero para saber sua tabuada: '))
    if num > 0:
        for c in range (1,11):
            print(f'{num} x {c} = {num*c}')
    else:
            break
print(f'FIM')

