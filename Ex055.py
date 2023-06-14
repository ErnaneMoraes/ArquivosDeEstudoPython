lista = ('primeira', 'segunda', 'terceira', 'quarta', 'quinta')
mai, men = 0, 0
for i in range (0,5):
    peso = float(input(f'Digite o peso da {lista[i]} pessoa: '))
    if i == 1:
        mai = peso
        men = peso
    else:
        if peso > mai:
            mai = peso
        elif peso < men:
            men = peso
print(f'Maior peso: {mai}\n'
      f'Menor peso: {men}')
