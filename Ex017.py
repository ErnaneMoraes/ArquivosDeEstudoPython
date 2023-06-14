'''op = float(input('Digite o tamanho do cateto oposto: '))
adj = float(input('Digite o tamano do cateto adjascente'))

hi = (op **2 + adj **2) ** (1/2)

print(f'A hipotenusa é: {hi}')'''

import math

op = float(input('Digite o tamanho do cateto oposto: '))
adj = float(input('Digite o tamano do cateto adjascente'))

hi = math.hypot(op,adj)

print(f'A hipotenusa é: {hi}')

