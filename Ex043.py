peso = float(input(f'Digite seu peso: '))
alt = float(input(f'Digite sua altura: '))

if peso == 0 or alt == 0:
    print(f'ENTRADA INVALIDA')
    peso = float(input(f'Digite seu peso: '))
    alt = float(input(f'Digite sua altura: '))
else:
    print(f'Seu IMC é: {imc:.2f}')

imc = peso / (alt ** 2)
if imc < 18.5:
    print(f'ABAIXO DO PESO')
elif imc < 25:
    print(f'PESO IDEAL')
elif imc < 30:
    print(f'SOBREPESO')
elif imc < 40:
    print(f'OBESIDADE')
elif imc >= 40:
    print(f'OBESIDADE MORBIDA')
else:
    print(f'ENTRADA INVALIDA')
