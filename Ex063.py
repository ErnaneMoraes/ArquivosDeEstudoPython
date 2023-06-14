n = int(input(f'Digite quantos termos voce quer mostrar: '))
n1 = 0
n2 = 1
i = 3
print(n1, '>', n2, '>', end=' ')
while i <= n:
    n3 = n1 + n2
    i += 1
    n1 = n2
    n2 = n3
    print(n3,'>', end=' ')
print(f'Fim')