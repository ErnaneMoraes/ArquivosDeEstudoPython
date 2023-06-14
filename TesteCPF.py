CPF = (input('Digite apenas o numeros do seu CPF: '))

tam = int(len(CPF))
tam2 = int(tam -2)
inic = int(CPF[0:tam2])

DV = int(CPF[tam2:tam])
print(inic,DV)

for i in range (0,tam):

    print(n[i])
    print(CPF[i])
