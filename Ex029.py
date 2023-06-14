vel = float(input(f'Digite a velocidade do carro: '))
multa =float((vel - 80) * 7)

if vel > 80:
    print(f'Você excedeu o limite de velocidade! Deverá pagar uma multa de R${multa:.2f}')
else:
    print(f'Boa viagem, mantenha a velocidade de acordo com a via!')