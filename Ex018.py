#Ex018

import math

ang = float(input('Digite o angulo que você deseja: '))

seno = math.sin(math.radians(ang))
print(f'Seno de {ang} = {seno:.2f}')

cos = math.cos(math.radians(ang))
print(f'Cosseno de {ang} = {cos:.2f}')

tan = math.tan(math.radians(ang))
print(f'Tangente de {ang} = {tan:.2f}')