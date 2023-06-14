nota1 = float(input(f'Digite a primeira nota do aluno: '))
nota2 = float(input(f'Digite a segunda nota do aluno: '))
nota = (nota1 + nota2) / 2

if nota >= 7:
    print(f'Aluno APROVADO')
elif nota < 7 and nota >= 5:
    print (f'Aluno de RECUPERAÇÃO')
else:
    print(f'Aluno REPROVADO')