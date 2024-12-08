from copy import deepcopy
from tqdm import tqdm

with open("i6.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = list(data[i])

dir = [
    [0,-1], ## starting position
    [1,0],
    [0,1],
    [-1,0]
]

for j,y in enumerate(data):
    for i,x in enumerate(y):
        if x == "^":
            start_x = i
            start_y = j
            start_dir = dir[0]

s = 0
r = []
r2 = []

pos_x  = start_x
pos_y = start_y
pos_dir = dir[0]

while(True):
    cond1 = (0 <= pos_x < len(data[0]))
    cond2 = (0 <= pos_y < len(data))
    if( (False == cond1) or (False == cond2) ):
        break
    else:
        if [pos_x,pos_y] not in r:
            r.append([pos_x,pos_y])
            r2.append([pos_x,pos_y,pos_dir])

    if (data[pos_y + pos_dir[1]][pos_x + pos_dir[0]] == "#"):
        pos_dir = dir[(dir.index(pos_dir) + 1 ) % len(dir)]
    else:
        pos_y += pos_dir[1]
        pos_x += pos_dir[0]

print(len(r))
        
for i, p in tqdm(enumerate(r2), initial=1, total=len(r2), desc="Processing"):

    data[p[1]][p[0]] = "#" 
    
    pos_x = r2[i - 1][0]
    pos_y = r2[i - 1][1]
    pos_dir = r2[i - 1][2]

    r3 = []

    while(True):
        cond1 = (0 <= (pos_x + pos_dir[0]) < len(data[0]))
        cond2 = (0 <= (pos_y + pos_dir[1]) < len(data))
        if( (False == cond1) or (False == cond2) ):
            data[p[1]][p[0]] = "." 
            break
        elif [pos_x,pos_y,pos_dir] in r3: # looping
            data[p[1]][p[0]] = "." 
            s += 1
            break
        else:
            r3.append([pos_x,pos_y,pos_dir])
        if (data[pos_y + pos_dir[1]][pos_x + pos_dir[0]] == "#"):
            pos_dir = dir[(dir.index(pos_dir) + 1 ) % len(dir)]
        else:
            pos_y += pos_dir[1]
            pos_x += pos_dir[0]

print(f"{s= }")
