import random

print(2 + 3 * 6 - 3)
print(2 ** 3)
print(2 + 5 * 6 / 2.2)
print(2 + 5 * 6 // 2.2)

x = 10
y = 6

z = x + y
z += x

totolotek = {12,25,33,41,12,33}
print(totolotek)

zbior = set()
def dodaj_liczby(liczba):
    zbior.add(liczba)
    print(zbior)

for i in range(5):
    dodaj_liczby(random.randint(1,10))


nowa_lista = list(zbior)
nowa_lista.sort()
print(nowa_lista)




