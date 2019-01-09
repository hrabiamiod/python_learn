print('Podaj liczbe')
liczba = input()

def collatz(a):
    while a != 1:               # Do kiedy a nie bedzie cyfra 1
        if a % 2 == 0:          # Jesli modulo wynosi zero
            a = a // 2          # dziel przez dwa
            print(a)
        elif a % 2 == 1:        # Jesli modulo wynosi jeden
            a = a * 3 + 1       # pomnoz przez 3 i dodaj 1
            print(a)


try:                            # Weryfikacjia czy input jest liczba
    b = int(liczba)
    collatz(b)
except ValueError:              # Jesli nie to
    print('Liczba musi być cyfrą!')l