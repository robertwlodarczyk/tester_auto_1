menu = """
        *****************
        *      MENU     *
        *****************
"""
print(menu)

imie = input("Podaj imię:").lower()
rok =  input("Podaj rok:")
# print(type(imie))
# print(type(rok))
lata = (rok,imie)
# print(type(lata))

if int (rok) < 2020:
    print("To jest data przed 2020...")
elif int (rok) > 2023:
    print("To jest data przyszła...")
    if imie == "Tomek".lower():
        print("To jest Tomek z przyszłości!")
else:
    print("Data między 2020 - 2023")

print("Zawartość krotki:", lata)

print(imie.count("o"))
print(imie.upper())
print(imie.lower())
print(lata.index("tomek"))

