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

wynik = 0

for i in range(len(dane)):
        wyniki = set(dane[i][0])
        wybory = set(dane[i][1])
        poprawne = list(wyniki.intersection(wybory))
        print(poprawne, len(poprawne))
        if len(poprawne) > 1:
            wynik += 2**(len(poprawne)-2)
        
print(wynik)