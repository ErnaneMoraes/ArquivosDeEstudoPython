
preco = float(input(f'Digite o valor do produto: '))
if type(preco) == int or float:
    pag = int(input(f'[1] - A vista \n'
                    f'[2] - A vista no cartao \n'
                    f'[3] - 2x no cartao \n'
                    f'[4] - 3x ou mais no cartao \n\n'
                    f'Digite o valor referente a forma de pagamento desejada: '))

    if pag == 1:
        valor = float(preco - ((preco / 100) * 10))
        print(f'O valor a ser pago é {valor:.2f}')
    elif pag == 2:
        valor = float(preco - ((preco / 100) * 5))
        print(f'O valor a ser pago é {valor:.2f}')
    elif pag == 3:
        parc = float(preco / 2)
        print(f'2 parcelas de {parc:.2f}')
    elif pag == 4:
        valor = float(preco + ((preco / 100) * 20))
        parc = float(valor / 3)
        print(f'Valor atualizado: {valor:.2f}, em 3 parcelas de {parc:.2f}')
    else:
        print(f'Entrada invalida')
else:
    print(f'ENTRADA INVALIDA')
