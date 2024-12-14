with open('i14.txt') as f:
    data = f.readlines()
pos = []
vel = []
YMAX = 103
XMAX = 101
for d in data:
    pos.append([int(x) for x in d.split(" ")[0].split("=")[1].split(",")])
    vel.append([int(x) for x in d.split(" ")[1].split("=")[1].split(",")])

for _ in range(100):
    for i,_ in enumerate(pos):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]

c = [0,0,0,0]
for i,_ in enumerate(pos):
    pos[i][0] = pos[i][0] % XMAX
    pos[i][1] = pos[i][1] % YMAX
    if pos[i][0] < XMAX // 2 and pos[i][1] < YMAX // 2:
        c[0] += 1
    elif pos[i][0] > XMAX // 2 and pos[i][1] < YMAX // 2:
        c[1] += 1
    elif pos[i][0] < XMAX // 2 and pos[i][1] > YMAX // 2:
        c[2] += 1
    elif pos[i][0] > XMAX // 2 and pos[i][1] > YMAX // 2:
        c[3] += 1

s = 1
for x in c:
    s *= x
print(f"{s= }")
