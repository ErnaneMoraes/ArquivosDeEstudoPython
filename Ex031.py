dist=float(input(f'Digite o tamanho da viagem em KM: '))

if dist <= 200:
    preco = dist * 0.50
    print(f'O valor da passagem é: {preco:.2f}')
else:
    preco = dist * 0.45
    print(f'O valor da passagem é: {preco:.2f}')
