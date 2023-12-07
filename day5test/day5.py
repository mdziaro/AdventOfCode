#import get_input
import time
def change_to_int(l):
    for i in range(len(l)):
        l[i]=int(l[i])
    return l
def proces(line,seeds, cch):
    for i in range(len(seeds)):
        if cch[i]:
            r = seeds[i] - line[1]
            if r >= 0 and r < line[2]:
                seeds[i]=line[0]+r
                cch[i]=False
    return seeds,cch

def change_seeds(s):
    seeds = set([seed for start, end in zip(s[::2], s[1::2]) for seed in range(start, start + end)])
    print(len(seeds))
    return list(seeds)


def change(lines):

    seeds = lines[0][:-1].split(" ")[1:]
    seeds = change_to_int(seeds)
    seeds = change_seeds(seeds)
    can_change = [True for _ in range(len(seeds))]
    for line in lines[1:]:
        line = line[:-1]
        line = line.split(" ")
        if len(line)==2 or len(line)==1 or len(line)==0:
            can_change = [True for _ in range(len(seeds))]
            continue
        else:
            line = change_to_int(line)
            seeds, can_change = proces(line,seeds, can_change)
    return min(seeds)

# lines = get_input.download_input(5)
file = open("input_day_5")
lines = file.readlines()
print(change(lines))