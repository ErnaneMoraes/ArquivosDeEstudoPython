cont2 = conti = conth = 0
rep = str('S')

while rep in 'SsYy':
    print(f'-'*20)
    print(f'CADASTRE UMA PESSOA')
    print(f'-'*20)

    idade = int(input(f'IDADE: '))
    print(f'-' * 20)
    sexo = input(f'Sexo: [M/F] ').upper()
    print(f'-' * 20)

    if idade >= 18:
        conti += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        cont2 += 1

    rep = str(input(f'QUER REPETIR? [S/N] ')).upper()

print(f'Quantas pessoas tem mais de 18 anos: {conti}')

print(f'Quantos homens foram cadastrados: {conth}')

print(f'Quantas mulheres tem menos de 20 anos: {cont2}')

print(f'Fim')
