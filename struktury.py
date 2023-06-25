dozwoloneWaluty = ("PLN","EUR","USD")
# waluta = input("Podaj walutę: ")
#
# if waluta in dozwoloneWaluty:
#     print("poprawna waluta")
# else:
#     print(f"Nieznany kod waluty, podano: {waluta}")
#

# Lista - dynamiczna (modyfikowalna)

lista = []
lista2 = ["Michał", "Ula", "Jacek"]

lista.append("Tomek")
lista.append("Robert")
lista.append("Mateusz")
lista.insert(1,"Zuzia")
lista.append(dozwoloneWaluty)
lista.pop(0)
lista.remove("Zuzia")
# lista.clear()
lista[0] = "Tomek"
lista.append(lista2)

# lista.sort()
# NIE SORTUJEMY LISTY KTÓRA MA RÓŻNE ELEMENTY
lista.reverse()

# zmienna = lista[1:4]
# ostatni = lista[-1][0]

print(lista)
# print(zmienna)
# print(ostatni)

