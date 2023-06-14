num = int(input(f'Digite um numero inteiro: '))

print(f'[1] Converter para BINÁRIO \n'
      f'[2] Converter para OCTAL \n'
      f'[3] Converter para HEXADECIMAL')

n1 = int(input(f'Sua opção: '))

if n1 == 1:
    print(f'{num} em binário é igual a {bin(num)[2:]}')
elif n1 == 2:
    print(f'{num} em octal é igual a {oct(num)[2:]}')
elif n1 == 3:
    print(f'{num} em hexadecimal é igual a {hex(num)[2:]}')
else:
    print(f'Opção invalida!')
