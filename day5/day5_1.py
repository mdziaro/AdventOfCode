plik = open("input5.txt", "r")
map1 = open("seed-to-soil.txt", "r")
map2 = open("soil-to-fertilizer.txt", "r")
map3 = open("fertilizer-to-water.txt", "r")
map4 = open("water-to-light.txt", "r")
map5 = open("light-to-temperature.txt", "r")
map6 = open("temperature-to-humidity.txt", "r")
map7 = open("humidity-to-location.txt", "r")

def odczytaj(plik):
    dane = plik.readlines()
    for i in range(len(dane)):
        if dane[i][-1] == "\n":
            dane[i] = dane[i][:-1]
        dane[i] = dane[i].split()
    return dane

dane = odczytaj(plik)
mapy = [map1, map2, map3, map4, map5, map6, map7]
for i in range(len(mapy)):
    mapy[i] = odczytaj(mapy[i])

seeds = list(map(int, dane[0][1:]))
print("maxxxxx:",max(seeds))
for j in range(len(mapy)):
    print(f"Processing map {j + 1}:")
    for i in range(len(seeds)):
        for k in range(len(mapy[j])):
            if (seeds[i] >= int(mapy[j][k][1])) and (seeds[i] < (int(mapy[j][k][1]) + int(mapy[j][k][2]))):
                seeds[i] = (seeds[i] - int(mapy[j][k][1])) + int(mapy[j][k][0])
                print(f"Seed {seeds[i]} after map {j + 1} transformation.")
                break
        

print("Final transformed seeds:", sorted(seeds))
print("Min location number:", min(seeds))
