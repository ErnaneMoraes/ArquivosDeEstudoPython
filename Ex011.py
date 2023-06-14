larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = larg*alt
tinta = area / 2

print(f'Sua parede tem as dimensões {larg} x {alt}, e sua área é {area}m²\n'
      f'Para pintar sua parede, você presisará de {tinta}L de tinta.')