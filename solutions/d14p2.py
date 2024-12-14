with open('i14.txt') as f:
    data = f.readlines()
pos = []
vel = []
YMAX = 103
XMAX = 101
for d in data:
    pos.append([int(x) for x in d.split(" ")[0].split("=")[1].split(",")])
    vel.append([int(x) for x in d.split(" ")[1].split("=")[1].split(",")])

def printpos(pos):
    X = [['1' for _ in range(YMAX)] for _ in range(XMAX)]
    for p in pos:
        X[p[0]][p[1]] = "0"
    for x in X:
        print("".join(x))
    print("\n")



for j in range(6870,6880):
    for i,_ in enumerate(pos):
        pos[i][0] += vel[i][0]
        pos[i][1] += vel[i][1]

        pos[i][0] = pos[i][0] % XMAX
        pos[i][1] = pos[i][1] % YMAX
    printpos(pos)
    print(j)
    input()
    

