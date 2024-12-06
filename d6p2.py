from copy import deepcopy
from tqdm import tqdm

with open("i6.txt") as f:
    data = f.readlines()

dir = [
    [0,-1], ## starting position
    [1,0],
    [0,1],
    [-1,0]
]

obstable_pos = []

for j,y in enumerate(data):
    for i,x in enumerate(y):
        if x == "^":
            start_x = i
            start_y = j
            start_dir = dir[0]

print(f"{start_x= } {start_y= }")


s = 0
r = []

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

    if (data[pos_y + pos_dir[1]][pos_x + pos_dir[0]] == "#"):
        pos_dir = dir[(dir.index(pos_dir) + 1 ) % len(dir)]
    else:
        pos_y += pos_dir[1]
        pos_x += pos_dir[0]
        
for i, p in tqdm(enumerate(r), total=len(r), desc="Processing"):

    data_copy = deepcopy(data)
    ## data_copy[p[0]][p[1]] = "#"
    data_copy[p[0]] = list(data_copy[p[0]])
    data_copy[p[0]][p[1]] = "#"
    data_copy[p[0]] = "".join(data_copy[p[0]])

    r2 = []

    pos_x = start_x
    pos_y = start_y
    pos_dir = start_dir

    while(True):
        cond1 = (0 <= (pos_x + pos_dir[0]) < len(data_copy[0]))
        cond2 = (0 <= (pos_y + pos_dir[1]) < len(data_copy))
        if( (False == cond1) or (False == cond2) ):
            break
        elif [pos_x,pos_y,pos_dir] in r2: # looping
            s += 1
            break
        else:
            r2.append([pos_x,pos_y,pos_dir])

        if (data_copy[pos_y + pos_dir[1]][pos_x + pos_dir[0]] == "#"):
            pos_dir = dir[(dir.index(pos_dir) + 1 ) % len(dir)]
        else:
            pos_y += pos_dir[1]
            pos_x += pos_dir[0]

print(f"{s= }")