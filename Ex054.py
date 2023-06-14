from datetime import date
anoatual = date.today().year

lista = ('primeira', 'segunda', 'terceira', 'quarta', 'quinta', 'sexta', 'setima')
mai, men = 0, 0

for i in range (0,7):
    anonasc = int(input(f'Em que ano a {lista[i]} pessoa nasceu? '))
    if anoatual - anonasc >= 18:
        mai += 1
    else:
        men += 1

print(f'Pessoas maiores de idade: {mai}\n'
      f'Pessoas menores de idade: {men}')
