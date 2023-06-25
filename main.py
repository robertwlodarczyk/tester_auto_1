from pakiet import kalkulator
from pakiet import  kalkulator as k
from pakiet import  human as h

# print("To jest główny plik...")
#
# kalkulator.mnozenie(10,2)
# kalkulator.dzielenie(50,2)
# k.mnozenie(22,3)
# k.dzielenie(102,43)
#
czlowiek1 = h.Human()
czlowiek1.imie = "Robert"
czlowiek1.plec = "m"
czlowiek1.wiek = 32
czlowiek1.powitanie()
czlowiek1.jaka_plec()
czlowiek1.ile_mam_lat()

czlowiek2 = h.Human2("Ewa",20,"k")
czlowiek2.powitanie()
czlowiek2.jaka_plec()
czlowiek2.ile_mam_lat()

czlowiek3 = h.Human2("Adam",25,"m")
czlowiek3.powitanie()
czlowiek3.jaka_plec()
czlowiek3.ile_mam_lat()

