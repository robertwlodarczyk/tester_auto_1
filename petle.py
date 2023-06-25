# jezyki = ["C","Python","Java"]
# cyfry = [1,2,3,4,5,6,7,8,9]
#
# print("Języki programowania:")
# for x in range(len(jezyki)):
#     print(jezyki[x])
#
# for x in range(0,len(cyfry),2):
#     print(f"Cyfry: {cyfry[x]}")
#
# print(*cyfry, sep="-")
# print(cyfry)
#
# for p in range(3):
#     for q in range(4):
#         if q == 2:
#             print(f'Pomijam q={q}')
#             continue
#     print(f'(p={p}, q={q})')
#
# i = 1
# tmp = 0
# while i <= 100:
#     tmp = tmp + i
#     i = i + i
# print("Suma liczba od 1 do 99", tmp)

while True:
    print("Menu:")
    print("1. policz")
    print("2. wyjdż")
    print("........")
    wybor = input("Wybierz opcje:")
    if wybor == "1":
        print("Suma:", 50 + 55)
    elif wybor == "2":
        break
    else:
        print("Nieznana opcja!")



