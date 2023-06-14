prim = int(input(f'Digite o primeiro termo: '))
raz = int(input(f'Digite a razão: '))
dec = prim + ((10 - 1) * raz)
for i in range (prim, dec + raz, raz):
    print(i, end=" ")
