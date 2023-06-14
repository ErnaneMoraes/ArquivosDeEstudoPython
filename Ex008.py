dist = float(input('Distancia em metros: '))
km = dist / 1000
mm = dist * 1000
cm = dist * 100

print(f'Em Km: {km}\n'
      f'Em Cm: {cm:.0f}\n'
      f'Em Mm: {mm:.0f}')
