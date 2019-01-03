import random

sekretnaLiczba = random.randint(1,20)
print('Zgadni liczbe od 1 do 20')

for guessesTaken in range(1, 7):
    print('Spróbuj podać liczbę.')
    guess = int(input())

    if guess < sekretnaLiczba:
        print('Za malo')
    elif guess > sekretnaLiczba:
        print('za duzo')
    else:
        break

if guess == sekretnaLiczba:
    print('Ok! Potrzebowales ' + str(guessesTaken) + ' prób')
else:
    print('Lipa, liczba to ' + str(sekretnaLiczba))

