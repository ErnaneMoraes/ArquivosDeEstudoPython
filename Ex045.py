from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')

opc = int(input(f'SUAS OPÇÕES: \n\n'
            f'[0] - PEDRA \n'
            f'[1] - PAPEL \n'
            f'[2] - TESOURA \n\n'
            f'QUAL SUA ESCOLHA? '))

if opc not in range(len(itens)):
    print('JOGADA INVÁLIDA')
else:

    print(f'JO')
    sleep(0.5)
    print(f'KEN')
    sleep(0.5)
    print(f'PO')

    comp = randint(0, 2)
    print('=-=' * 10)
    print(F'Computador jogou: {itens[comp]}')
    print(F'Jogador jogou: {itens[opc]}')
    print('=-=' * 10)

    if comp == 0:
        if opc == 0:
            print(f'EMPATE')
        elif opc == 1:
            print(f'JOGADOR VENCE')
        elif opc == 2:
            print(f'COMPUTADOR VENCE')
    elif comp == 1:
        if opc == 0:
            print(f'COMPUTADOR VENCE')
        elif opc == 1:
            print(f'EMPATE')
        elif opc == 2:
            print(f'JOGADOR VENCE')
    elif comp == 2:
        if opc == 0:
            print(f'JOGADOR VENCE')
        elif opc == 1:
            print(f'COMPUTADOR VENCE')
        elif opc == 2:
            print(f'EMPATE')
    else:
            print(f'JOGADA INVALIDA')