plik = open("input3.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]

symbols = ["*", "#", "$", "/", "@", "=", "+", "-"]
symbol_locations = []
number_locations = []

for i in range(len(dane)):
    for j in range(len(dane[i])):
        if dane[i][j] in symbols:
            symbol_locations.append((i, j))

for i in range(len(dane)):
    flag = 0
    for j in range(len(dane[i])):
        if dane[i][j].isnumeric():
            if flag == 0:
                number_locations.append([[i, j], dane[i][j]])
                flag = 1
            else:
                number_locations[-1][1] = str(number_locations[-1][1]) + str(dane[i][j])
        else:
            if flag:
                number_locations.append([[i,j+len(number_locations[-1][1])],number_locations[-1][1]])
            flag = 0

wynik = 0


def loc_offset(location, offset):
    locations = location.copy()
    for i in range(len(locations)):
        locations[i] = [locations[i][0] + offset[0], locations[i][1] + offset[1]]
    return locations


symbol_locations1 = loc_offset(symbol_locations, [-1, -1])
symbol_locations2 = loc_offset(symbol_locations, [-1, 0])
symbol_locations3 = loc_offset(symbol_locations, [-1, 1])
symbol_locations4 = loc_offset(symbol_locations, [0, -1])
symbol_locations5 = loc_offset(symbol_locations, [0, 1])
symbol_locations6 = loc_offset(symbol_locations, [1, -1])
symbol_locations7 = loc_offset(symbol_locations, [1, 0])
symbol_locations8 = loc_offset(symbol_locations, [1, 1])

for i in range(len(number_locations)):
    if number_locations[i][0] in symbol_locations1:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations2:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations3:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations4:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations5:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations6:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations7:
        wynik += int(number_locations[i][1])
    elif number_locations[i][0] in symbol_locations8:
        wynik += int(number_locations[i][1])

print(wynik)
