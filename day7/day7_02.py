import collections
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
numbers = {"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}

def hand_type(hand):
    common = collections.Counter(hand).most_common(1)[0]
    hand_copy = hand
    if common[0] != "J":
        hand_copy = hand.replace("J", common[0])
    else:
        if hand.count("J") != 5:
            hand_copy = hand.replace("J", collections.Counter(hand).most_common(2)[1][0])
    if len(set(hand_copy)) == 1:
        return "five" 
    elif len(set(hand_copy)) == 2:
        if hand_copy.count(hand_copy[0]) == 1 or hand_copy.count(hand_copy[0]) == 4:
            return "four" 
        else:
            return "full" 
    elif len(set(hand_copy)) == 3:
        if hand_copy.count(hand_copy[0]) == 3 or hand_copy.count(hand_copy[1]) == 3 or hand_copy.count(hand_copy[2]) == 3:
            return "three"
        else:
            return "two"
    elif len(set(hand_copy)) == 4:
        return "pair"
    else:
        return "high"

for i in range(len(dane)):
    dane[i].append(dict_tiers[hand_type(dane[i][0])])
#"""
for i in range(len(dane)):
    value = 0
    for j in range(5):
        value += numbers[dane[i][0][j]] * len(numbers)**(5-j)
    dane[i][0] = value
#"""
dane.sort(key=lambda hand: hand[0])        
dane.sort(key=lambda hand: hand[2])


wynik = 0
for i in range(1, len(dane)+1):
    wynik += int(dane[i-1][1]) * i

print(dane)
print(wynik)
