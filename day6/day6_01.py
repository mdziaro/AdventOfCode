plik = open("input6.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]

czas = list(map(int,dane[0].split()[1:]))
dystans = list(map(int,dane[1].split()[1:]))
print(dystans)
count = []

for i in range(len(czas)):
    licznik = 0
    for j in range(czas[i]):
        if j*(czas[i]-j) > dystans[i]:
            licznik += 1
    count.append(licznik)
print(count)
