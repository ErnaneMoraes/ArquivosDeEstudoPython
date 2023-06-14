from time import sleep

num = int(input(f'Digite um numero para ver sua tabuada: '))

for i in range (1, 11):
    print(f'-' * 15)
    print(num,'x',i,'=',num * i)
    sleep(0.5)
print(f'Fim')
