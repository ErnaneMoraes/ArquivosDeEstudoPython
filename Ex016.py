import math

num = float(input('Digite um valor: '))
int = int(num)

print (f'O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}\n'
       f'Arredondando pra cima: {math.ceil(num)}\n'
       f'Arredondando pra baixo: {math.floor(num)}')
