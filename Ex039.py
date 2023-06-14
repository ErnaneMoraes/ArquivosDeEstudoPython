from datetime import date
atual = date.today().year
nasc = int(input(f'Digite o ano que você nasceu: '))
idade = atual - nasc
sexo = str(input(f'Digite M para sexo MASCULINO e F para FEMININO: '))

if sexo == 'F':
    print(f'Você não precisa se alistar!')
elif sexo == 'M':
    if idade == 18:
        print(f'Você deve se alistar IMEDIATAMENTE!')
    elif idade < 18:
        print(f'Você não tem 18 anos, ainda faltam {18 - idade} anos para seu alistamento')
    else:
        print(f'Você tem {idade}, já devetria ter se alistado a {idade - 18} anos')
else:
    print('Entrada inválida')
