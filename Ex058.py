from random import randint
from time import sleep

num = randint(0, 5)

print('Pensei em um numero entre 0 e 10, tente adivinhar!')
guess = int(input('Qual seu palpite? '))
c = 1

while guess != num:
    print('PROCESSANDO...')
    sleep(1)
    c += 1
    if num > guess:
        guess = int(input(f'Mais... Tente novamente: '))
    else:
        guess = int(input(f'Menos... Tente novamente: '))

print('PROCESSANDO...')
sleep(1)
print(f'Parabéns, você acertou com {c} tentativas! O numero era {num}!')
