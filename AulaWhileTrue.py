soma = cont = 0

while True:
    n1 = int(input(f'Digite um numero: '))

    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'O programa rodou {cont} vezes, a soma dos numeros é igual a {soma}')

