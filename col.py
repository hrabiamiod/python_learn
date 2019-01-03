print('Podaj liczbe')
a = int(input())

while a != 1:
    if a % 2 == 0:
        a = a // 2
        print(a)
    elif a % 2 == 1:
        a = a * 3 + 1
        print(a)
