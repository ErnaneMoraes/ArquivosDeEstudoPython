numero = int(input("Digite um número de 0 a 9: "))

# verifica se o número está dentro do intervalo válido
if numero < 0 or numero > 9:
    print("Número inválido!")
else:
    print(f"Tabuada de multiplicação do número {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")