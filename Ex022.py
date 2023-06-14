nome = input('Digite seu nome completo: ').strip()

print(f'Seu nome em minusculo: {nome.lower()}')

print(f'Seu nome em maiusculo: {nome.upper()}')

print(f'Tamano do seu nome sem contar os espaços: {len(nome)-nome.count(" ")}')