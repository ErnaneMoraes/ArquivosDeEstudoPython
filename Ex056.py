lista = ('Primeira', 'Segunda', 'Terceira', 'Quarta')
media = float(0)
qtdmenor = 0
maisvelho = str()
idmaisvelho = int(0)

for i in range (0,4):
    print('~' * 10, f' {lista[i]} pessoa: ', '~' * 10)
    nome_pessoa = str(input(f'Nome: '))
    idade_pessoa = int(input(f'Idade: '))
    sexo_pessoa = str(input(f'Sexo: '))
    media += idade_pessoa

    if sexo_pessoa == 'F':
        if idade_pessoa < 20:
            qtdmenor += 1
    elif idade_pessoa > idmaisvelho:
        idmaisvelho = idade_pessoa
        maisvelho = nome_pessoa

print(f'O homem mais velho se chama {maisvelho}, ele tem {idmaisvelho} anos.\n'
      f'{qtdmenor} mulheres tem menos de 20 anos.\n'
      f'A media de idades é: {media / 4}')