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
curr_location = []

for i in range(2, len(dane)):
    direction = (dane[i][2][1:4],dane[i][3][:3])
    directions.update({dane[i][0]:direction})

steps = 0
how_many_starting_positions = 0
for i in range(2, len(dane)):
    if dane[i][0][-1] == "A":
        how_many_starting_positions += 1
        curr_location.append(dane[i][0])


def check_result(array):
    for i in range(len(array)):
        if array[i][-1] != "Z":
            return True
    return False

count = 0
multipliers = [0,0,0,0,0,0]
while True:
    #print(curr_location)
    for i in range(how_many_starting_positions):
        if turns[steps] == "R":
            side = 1
        else:
            side = 0
        curr_location[i] = directions[curr_location[i]][side]
        if multipliers[i] == 0:
            if curr_location[i][-1] == "Z":
                multipliers[i] = steps+1
                count += 1
    steps+=1
    
    if count == len(curr_location):
        break
print(steps)
print(multipliers)
from math import lcm

print(lcm(*multipliers))
