plik = open("input5.txt", "r")

def odczytaj(plik):
    dane = plik.readlines()
    for i in range(len(dane)):
        if dane[i][-1] == "\n":
            dane[i] = dane[i][:-1]
        dane[i] = dane[i].split()
    return dane


dane = odczytaj(plik)
seeds = list(map(int, dane[0][1:]))
#print(dane)
#print(seeds)

mapy = []

for i in range(1, len(dane)):
    if dane[i] == []:
        mapy.append([])
    elif dane[i-1] == []:
        pass
    else:
        mapy[-1].append(list(map(int,dane[i])))

for i in range(len(mapy)):
    for j in range(len(seeds)):
        #print(mapy[i])
        for k in range(len(mapy[i])):
            dst, src, rng = mapy[i][k][0],mapy[i][k][1],mapy[i][k][2]
            if seeds[j] >= src and seeds[j] < src+rng:
                seeds[j] = seeds[j] - (src - dst)
                break
print(sorted(seeds))