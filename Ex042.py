r1 = float(input(f'Digite o primeiro lado do triangulo: '))
r2 = float(input(f'Digite o segundo lado do triangulo: '))
r3 = float(input(f'Digite o terceiro lado do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
        print(f'Os segmentos podem formar um triangulo EQUILATERO')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print(f'Os segmentos podem formar um triangulo ESCALENO')
    else:
        print(f'Os segmentos podem formar um triangulo ISOCELES')
else:
    print(f'Os segmentos não podem formar um triangulo')