nome = str(input('Digite seu nome completo: ')).strip()
snome = nome.split()

print(f'Primeiro nome: {snome[0]}\n'
      f'Ultimo nome: {snome[len(snome)-1]}')