valorhora = float(input('Digite o valor/hora do funcionário: R$'))
aumento = float(input('Digite a porcentagem do aumento do salário: '))

salario = valorhora * 220
aumentototal = 100 + aumento
salarionovo = (salario/100) * aumentototal

print(f'\nEste funcionário recebe atualmente R${salario:.2f}\n'
      f'Seu salário com um aumento de {aumento:.0f}% é igual à R${salarionovo:.2f}')