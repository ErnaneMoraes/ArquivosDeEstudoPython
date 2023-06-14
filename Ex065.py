
resp = 'S'
n1 = c = soma = mai = men = 0
while resp == 'S':
    n1 = int(input(f'Digite um numero: '))
    resp = str(input(f'Quer continuar? [S/N]')).upper()
    c += 1
    soma +=n1
    if c == 1:
        mai = men = n1
    else:
        if n1 > mai:
            mai = n1
        if n1 < men:
            men = n1
media = float(soma / c)
print(f'Você digitou {c} numeros, a media é {media:.2f}\n'
      f'O maior numero é {mai} e o menor {men}')
