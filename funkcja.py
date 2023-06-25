def drukuje():
    print("drukuje...")

def dodawanie(a,b=0):
    suma = a +b
    return suma

print("A tutaj coś innego z programu głównego..")

for i in range(5):
    drukuje()


wyniki = []
wyniki.append(dodawanie(5,5))
wyniki.append(dodawanie(22,533))
wyniki.append(dodawanie(525252,2342432))
wyniki.append(dodawanie(525252))

# argumenty domyślne nie mogą być przed wymaganymi

print(wyniki)