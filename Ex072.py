num  = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'desenove', 'vinte',)

while True:
    n1 = int(input(f'Digite o numero que quer saber: '))
    if 0 <= n1 <= 20:
        break
    print(f'Tente novamente')

print(num[n1])
