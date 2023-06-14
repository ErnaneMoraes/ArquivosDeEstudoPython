cont = conti = menp = 0
rep = str('S')
valor = total = float(0)
nome1 = ' '

while rep in 'SsYy':
    cont += 1
    print(f'-'*20)
    print(f'NOME E PREÇO')
    print(f'-'*20)

    nome = str(input(f'Digite o nome do produto: '))
    print(f'-' * 20)
    preco = float(input(f'Digite o preço do produto: '))
    print(f'-' * 20)

    total += preco

    if cont == 1:
        menp = preco
        nome1 = nome
    if preco < menp:
        menp = preco
        nome1 = nome
    if preco > 1000:
        conti += 1

    rep = str(input(f'QUER REPETIR? [S/N] ')).upper()

print(f'O total gasto na compra: {total}')

print(f'quantos produtos custam mais de R$1000: {conti}')

print(f'Qual é o nome do produto mais barato: {nome1}')

print(f'Fim')
