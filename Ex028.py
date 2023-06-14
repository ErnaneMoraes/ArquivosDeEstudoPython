from random import randint
from time import sleep

num=randint(0, 5)

print('Pensei em um numero entre 0 e 5, tente adivinhar!')
guess=int(input('Qual seu palpite? '))

print('PROCESSANDO...')
sleep(2)

if guess == num:
    print(f'Parabéns, você acertou! O numero era {num}!')
else:
    print(f'Errou! O numero era {num}!')

