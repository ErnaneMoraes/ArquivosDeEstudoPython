prim = int(input(f'Digite um numero: '))

c = 0
for i in range (1, prim +1):
    if prim % i == 0:
        c += 1
if c == 2:
    print(f'PRIMO')
    exit()
else:
    print(f'NAO PRIMO')
    exit()
