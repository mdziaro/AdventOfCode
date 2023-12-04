plik = open("input4.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]
    indeks = dane[i].index(":")
    dane[i] = dane[i][indeks+1:]
    dane[i] = dane[i].split("|")
    dane[i][0] = dane[i][0].split(" ")
    dane[i][1] = dane[i][1].split(" ")

war_wyniki = []

for i in range(len(dane)):
        wyniki = set(dane[i][0])
        wybory = set(dane[i][1])
        poprawne = list(wyniki.intersection(wybory))
        print(poprawne, len(poprawne))
        war_wyniki.append(len(poprawne)-1)
        
print(war_wyniki)
wynik = 0
for i in range(len(war_wyniki)):
     war_wyniki[i] = [1, war_wyniki[i]]
print(war_wyniki)

for i in range(len(war_wyniki)):
    wynik += war_wyniki[i][0] # wynik += ilość kopii
    for j in range(1,war_wyniki[i][1]+1): # 
        war_wyniki[i+j][0] += war_wyniki[i][0]
print(wynik)
print(war_wyniki)