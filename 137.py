spam = ['jabłka', 'banay', 'tofu', 'koty']      ## definicja listy

inakoniec = len(spam) - 1                       ## obliczenie przedostaniego elementu

spam.insert(inakoniec, 'i')                     ## dodanie do listy na przedostatnim miejscu litery i

for i in range(0, len(spam)):                   ## petelka wyswietlajaca liste w linii
    print (spam[i], end=' ')