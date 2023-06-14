
n1 = int(input(f'Digite o primeiro numero: '))
n2 = int(input(f'Digite o segundo numero: '))

opc = 0
c = 0

while opc != 5:
      opc = int(input(f'[1] - Somar \n'
                      f'[2] - Multiplicar \n'
                      f'[3] - Maior \n'
                      f'[4] - Novos numeros \n'
                      f'[5] - Sair do programa \n'
                      f'Digite a opção desejada: '))
      if opc == 1:
            res = n1 + n2
            print(f'{n1} + {n2} = {res}')
      elif opc == 2:
            res = n1 * n2
            print(f'{n1} x {n2} = {res}')
      elif opc == 3:
            if n1 > n2:
                  print(f'{n1} é maior que {n2}')
            elif n1 < n2:
                  print(f'{n2} é maior que {n1}')
            else:
                print(f'Os dois numeros são iguais.')
      elif opc == 4:
            n1 = int(input(f'Digite o primeiro numero: '))
            n2 = int(input(f'Digite o segundo numero: '))
      elif opc == 5:
          print(f'Finalizando...')
      else:
            print(f'Opção invalida')
