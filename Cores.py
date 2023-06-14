valorCasa = float(input(f'Digite o valor da casa que deseja comprar: '))
salario = float(input(f'Digite o seu salário: '))
prazo = float(input(f'Digite em quantos anos deseja pagar: '))

numparc = prazo * 12
valparc = valorCasa / numparc
porcsal = (salario / 100) * 30

# print(f' Numero de parcelas: {numparc:.2f},\n'
#       f' Valor das parcelas: {valparc:.2f}, \n'
#       f' 30% do salario: R${porcsal:.2f}')

if valparc < porcsal:
      print(f'Parabéns! Seu empréstimo foi APROVADO! \n'
            f'Valor das parcelas: R${valparc:.2f}')
else:
      print(f'Empréstimo NEGADO!!!')
