from time import sleep

c = 1

while c != 10:
    print(c, end=(' '))
    c += 1
    sleep(0.5)
print('fim')