from datetime import date
nasc = int(input(f'Digite o ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade > 25:
    print(f'MASTER')
elif idade > 19 and idade <= 25:
    print(f'SENIOR')
elif idade > 14 and idade <= 19:
    print(f'JUNIoR')
elif idade > 9 and idade <= 14:
    print(f'INFANTIL')
elif idade <= 9:
    print(f'MIRIM')
else:
    print(f'ENTRADA INVALIDA')
