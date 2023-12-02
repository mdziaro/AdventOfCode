plik = open("input2.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i]=dane[i][:-1]
    indeks = dane[i].index(":")
    dane[i] = dane[i][indeks+1:]
    dane[i] = dane[i].split(";")

colors = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}


def find_value(string, color):
    try:
        indeks = string.index(color)
        number = int(string[indeks-3:indeks])
        return number
    except ValueError:
        return 1

round = []
power = 0
flag = 0

for i in range(len(dane)):
    flag = 0
    print(dane[i])
    red = []
    green = []
    blue = []
    for j in range(len(dane[i])):
        round = dane[i][j]
        red.append(find_value(round, "red"))
        green.append(find_value(round, "green"))   
        blue.append(find_value(round, "blue"))
    red = max(red) 
    green = max(green)         
    blue = max(blue) 
    power += red*green*blue      
print(power)          