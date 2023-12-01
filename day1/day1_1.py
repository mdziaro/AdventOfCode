plik = open("input1.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i]=dane[i][:-1]
print(dane)


wyniki = []

for i in range(len(dane)):
    flag1 = 0
    wynik = ""
    temp = ""
    for j in range(len(dane[i])):

        if (not flag1 and dane[i][j].isnumeric()):
            flag1 = 1
            wynik += dane[i][j]
        elif dane[i][j].isnumeric():
            temp = dane[i][j]
    wynik += temp
    if len(wynik) == 1:
        wynik *= 2
    wyniki.append(wynik)


suma = 0
for i in wyniki:
    suma += int(i)

print(suma)