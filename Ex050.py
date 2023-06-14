lista = ('primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto')
soma = 0
for i in range (0, 6):
    num = int(input(f'Digite o {lista[i]} numero: '))
    if num % 2 == 0:
        soma += num
print(f'A soma dos numeros pares digitados é igual a: {soma}')
