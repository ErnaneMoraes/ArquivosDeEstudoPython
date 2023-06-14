dias = int(input('Digite a quantidade de dias: '))
dist = float(input('Digite a Km percorrida: '))

preco = (dist * 0.15) + (60 * dias)

print(f'O valor a ser pagado é R${preco:.2f}')
