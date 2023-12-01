plik = open("input1.txt", "r")
dane = [line.strip() for line in plik.readlines()]
plik.close()

def is_valid(x, numbers):
    if x in numbers:
        return True
    return False 

numbers = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

wyniki = []

for i in range(len(dane)):
    flag1 = 0
    wynik = ""
    temp = ""
    for j in range(len(dane[i])):
        if (not flag1 and dane[i][j].isnumeric()):
            flag1 = 1
            wynik += dane[i][j]
        elif (not flag1 and dane[i][j].isalpha()):
            for k in range(3, 6):
                if is_valid(dane[i][j:j+k], numbers):
                    wynik += str(numbers[dane[i][j:j+k]])
                    flag1 = 1
                    break
        elif dane[i][j].isnumeric():
            temp = dane[i][j]
        elif dane[i][j].isalpha():
            for k in range(3, 6):
                if is_valid(dane[i][j:j+k], numbers):
                    temp = str(numbers[dane[i][j:j+k]])
                    break
    if temp != "":
        wynik += temp
    print(wynik)
    if len(wynik) == 1:
        wynik *= 2
    print(wynik)
    wyniki.append(wynik)

suma = 0
for i in wyniki:
    suma += int(i)

print(suma)
