n1 = int(input(f'Digite o primeiro valor: '))
n2 = int(input(f'Digite o segundo valor: '))
n3 = int(input(f'Digite o terceiro valor: '))

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print (f'O maior numero é: {maior}!\n'
       f'O menor numero é: {menor}!')




