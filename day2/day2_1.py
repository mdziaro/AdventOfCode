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
suma = 0
flag = 0

for i in range(len(dane)):
    flag = 0
    for j in range(len(dane[i])):
            round = dane[i][j]
            if find_value(round, "red")>colors["red"] or find_value(round, "green")>colors["green"] or find_value(round, "blue")>colors["blue"]:
                print(dane[i])
                print(round)
                print(find_value(round, "red"),find_value(round, "green"),find_value(round, "blue"))
                flag = 0
                break
            flag = 1 
    if flag:
        suma += i+1
print(suma)