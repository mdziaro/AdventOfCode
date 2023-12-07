plik = open("input7.txt")

def odczytaj(plik):
    dane = plik.readlines()
    for i in range(len(dane)):
        if dane[i][-1] == "\n":
            dane[i] = dane[i][:-1]
        dane[i] = dane[i].split()
    return dane

dane = odczytaj(plik)

dict_tiers = {"five": 7, "four": 6, "full": 5, "three": 4, "two": 3, "pair": 2, "high":1}
numbers = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}

def hand_type(hand):
    if len(set(hand)) == 1:
        return "five"
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            return "four"
        else:
            return "full"
    elif len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            return "three"
        else:
            return "two"
    elif len(set(hand)) == 4:
        return "pair"
    else:
        return "high"

for i in range(len(dane)):
    dane[i].append(dict_tiers[hand_type(dane[i][0])])

for i in range(len(dane)):
    value = 0
    for j in range(5):
        value += numbers[dane[i][0][j]] * len(numbers)**(5-j)
    dane[i][0] = value

dane.sort(key=lambda hand: hand[0])        
dane.sort(key=lambda hand: hand[2])


wynik = 0
for i in range(1, len(dane)+1):
    wynik += int(dane[i-1][1]) * i

print(dane)
print(wynik)
