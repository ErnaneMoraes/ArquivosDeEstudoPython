frase = str(input(f'Digite uma frase: ')).strip().upper()
var1 = frase.split()
var2 = ''.join(var1)
inv = ''

for i in range (len(var2) - 1, -1, -1):
    inv += var2[i]

if inv == var2:
    print(f'PALINDROMO')
else:
    print(f'NAO PALINDROMO')
print(inv, var2)