plik = open("input6.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]

czas = list(dane[0].split()[1:])
dystans = list(dane[1].split()[1:])

for i in range(1, len(czas)):
    czas[0] += czas[i]
    dystans[0] += dystans[i]
dystans = int(dystans[0])
czas = int(czas[0])
print(dystans)
print(czas)
count = 0


for j in range(czas):
    if j*(czas-j) > dystans:
        count += 1

print(count)