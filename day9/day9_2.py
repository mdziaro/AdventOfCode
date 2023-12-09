plik = open("input9.txt")
from time import sleep
def odczytaj(plik):
    dane = plik.readlines()
    for i in range(len(dane)):
        if dane[i][-1] == "\n":
            dane[i] = dane[i][:-1]
        dane[i] = dane[i].split()
    return dane

def extrapolate(data):
    sub_values = ["0"]*(len(data)-1)
    for j in range(len(data)-1):
        sub_values[j] = data[j+1]-data[j]
    return sub_values

dane = odczytaj(plik)

wynik = 0

for i in range(len(dane)):
    values = [dane[i]]
    values[-1] = list(map(int,values[-1]))
    while True:
        values.append(extrapolate(values[-1]))
        if set(values[-1]) == set([0]):
            break
    for j in range(len(values)-2, -1, -1):
        values[j][0] = int(values[j][0])-int(values[j+1][0])
    print(values[0][0])
    print(values)
    wynik += int(values[0][0])
print(wynik)
    