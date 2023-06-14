n1 = 0
c = 0
soma = 0
n1 = int(input(f'Digite um numero: '))
while n1 != 999:
    c += 1
    soma += n1
    n1 = int(input(f'Digite um numero: '))
print(f'Você digitou {c} numeros, a soma é {soma}')

