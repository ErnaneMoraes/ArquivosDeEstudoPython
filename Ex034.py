salario = float(input(f'Digite seu salario: '))

if salario < 1250 :
    porc = int(15)
    aumento = (salario / 100) * 15
    salario = salario + aumento

    print(f'Seu salário rcebeu um aumento de {porc}%, salario atualizado: R${salario:.2f}')
else:
    porc = int(10)
    aumento = (salario / 100) * 10
    salario = salario + aumento

    print(f'Seu salário rcebeu um aumento de {porc}%, salarioa atualizado: R${salario:.2f}')

