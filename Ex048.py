s = 0
c = 0
for i in range (1, 501, 2):
    if i % 3 == 0:
        print (i, end=" ")
        s += i
        c += 1
print(f'\nA soma de todos os {c} valores solicitados é: {s}')