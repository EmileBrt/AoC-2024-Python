from tqdm import tqdm
from copy import deepcopy

with open("i7.txt") as f:
    d = f.readlines()

def rec_search(goal, l):
    if len(l) == 1:
        if l[0] == goal:
            return 1
        else:
            return 0
    for x in l:
        if x > goal:
            return 0
    
    # LEFT TO RIGHT READ THE CHALLENGE YOU DUMBASS
    m = l.pop(0)
    l1 , l2 = deepcopy(l), deepcopy(l)
    l1[0], l2[0] = l1[0] *m, l2[0] + m
    return max(rec_search(goal,l1 ), rec_search(goal,l2))

for i,_ in enumerate(d):
    d[i] = d[i].split(": ")
    d[i][0],d[i][1] = int(d[i][0]), [int(x) for x in d[i][1].replace("\n","").split(" ")]
        
s=0
for i, _ in tqdm(enumerate(d), total=len(d), desc="Processing"):
    if 1 == rec_search(d[i][0],d[i][1]):
        s += d[i][0]
print(f"{s= }")