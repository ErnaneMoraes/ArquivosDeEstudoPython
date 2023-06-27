num = (int(input(f'Digite um numero: ')),
       int(input(f'Digite mais um numero: ')),
       int(input(f'Digite mais um numero: ')),
       int(input(f'Digite mais um numero: ')),
       int(input(f'Digite o ultimo numero: ')), )

print(num)
print(f'O numero 9 apareceu {num.count(9)} vezes')

if 3 in num:
       print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
       print(f'O valor 3 não foi digitado')

print(f'Numeros pares digitados: ', end=' ')
for n in num:
       if n % 2 == 0:
              print (n, end=' ')