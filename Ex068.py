from time import sleep
from random import randint

while True:
    print(f'-'*30)
    opc = int(input(f'Digite 1 para impar e 2 para par: '))
    comp = randint(1, 10)
    if opc % 2 == 0:
        print(f'Você escolheu PAR, então eu sou IMPAR! \n'
              f'3... 2... 1...')
        sleep(1)
        print(f'O resultado é...')
        sleep(1)
        print(f'{comp}!')
        if comp % 2 == 0:
            print(f'O resultado foi PAR, você ganhou!')
            break
        else:
            print(f'O resultado foi IMPAR, você perdeu!')
    else:
        print(f'Você escolheu IMPAR, então eu sou PAR! \n'
              f'3... 2... 1...')
        sleep(1)
        print(f'O resultado é...')
        sleep(1)
        print(f'{comp}!')
        if comp % 2 == 0:
            print(f'O resultado foi PAR, você perdeu!')
        else:
            print(f'O resultado foi IMPAR, você ganhou!')
            break
print(f'FIM DE JOGO')
