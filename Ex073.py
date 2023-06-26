times = ( 'Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
          'Atletico MG', 'Botafogo', 'Atletico PR', 'Bahia', 'Sao paulo', 'Fluminense', 'Sport Recife', 'Vitoria',
          'Coritiba', 'Avai', 'Ponte preta', 'Atletico GO',)

print(f'-=' * 15)
print(f'Lista de times {times}')
print(f'-=' * 15)
print(f'Os 6 primeiros são: {times[0:5]}')
print(f'-=' * 15)
print(f'Os 4 ultimos são: {times[-4:]}')
print(f'-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'-=' * 15)
print(f'Posição do chapecoense: {times.index("Chapecoense")+1}')