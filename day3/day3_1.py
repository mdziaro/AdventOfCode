plik = open("input3.txt", "r")
dane = plik.readlines()
for i in range(len(dane)):
    if dane[i][-1] == "\n":
        dane[i] = dane[i][:-1]

dane.append("."*len(dane[0]))
dane = ["."*len(dane[0])]+(dane)
for i in range(len(dane)):
    dane[i] = "."+dane[i]+"."
print(dane)


print(len(dane))
print(len(dane[0]))
wynik = 0
flag = 0
for i in range(0, len(dane)):
    number = 0
    for j in range(0, len(dane[i])):
        if dane[i][j].isdigit() and not (dane[i][j-1].isdigit()):
            number += int(dane[i][j])
            if dane[i][j+1].isdigit():
                number *= 10
                number += int(dane[i][j+1])
                if dane[i][j+2].isdigit():
                    number *= 10
                    number += int(dane[i][j+2])
                    if dane[i][j+3].isdigit():
                        number *= 10
                        number += int(dane[i][j+3])
        if number != 0:
            for k in range(0, 3):
                for l in range(0, len(str(number))+2):
                    if not dane[i+k-1][j+l-1].isdigit() and not dane[i+k-1][j+l-1] == ".":
                        flag = 1
            if flag == 1:
                wynik += number
                flag = 0
            number = 0
        
                

print(wynik)