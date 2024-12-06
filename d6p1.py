with open("i6.txt") as f:
    data = f.readlines()

dir = [
    [0,-1], ## starting position
    [1,0],
    [0,1],
    [-1,0]
]

for j,y in enumerate(data):
    for i,x in enumerate(y):
        if x == "^":
            pos_x = i
            pos_y = j
            pos_dir = dir[0]

print(f"{pos_x= } {pos_y= }")

r = set()

while(True):
    cond1 = (0 <= pos_x < len(data[0]))
    cond2 = (0 <= pos_y < len(data))
    if( (False == cond1) or (False == cond2) ):
        break
    else:
        r.add(f"[{pos_x},{pos_y}]")

    if (data[pos_y + pos_dir[1]][pos_x + pos_dir[0]] == "#"):
        pos_dir = dir[(dir.index(pos_dir) + 1 ) % len(dir)]
    else:
        pos_y += pos_dir[1]
        pos_x += pos_dir[0]
        
s = len(r)
print(f"{s= }")