prim = int(input(f'Digite o primeiro termo: '))
raz = int(input(f'Digite a razão: '))
termo = prim
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print(termo, end=" ")
        termo += raz
        cont += 1

    mais = int(input(f'\nDeseja mostrar mais quantos termos? '))
print(f'Foram mostrados {cont-1} termos')