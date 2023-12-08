plik = open("input8.txt")

def odczytaj(plik):
    dane = plik.readlines()
    for i in range(len(dane)):
        if dane[i][-1] == "\n":
            dane[i] = dane[i][:-1]
        dane[i] = dane[i].split()
    return dane

dane = odczytaj(plik)
turns = dane[0][0]*len(dane)*len(dane)
#print(turns)
directions = {}
curr_location = "AAA"

for i in range(2, len(dane)):
    direction = (dane[i][2][1:4],dane[i][3][:3])
    directions.update({dane[i][0]:direction})

steps = 0
while curr_location != "ZZZ":

    if turns[steps] == "R":
        side = 1
    else:
        side = 0
    curr_location = directions[curr_location][side]
    steps+=1
print(steps)
print(curr_location)