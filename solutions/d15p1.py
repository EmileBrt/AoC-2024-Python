with open("i15.txt") as f:
    data = f.readlines()

m = [x.replace("\n","") for x in data[:50]]
path = ''.join([x.replace("\n","") for x in data[52:]])

for i,_ in enumerate(m):
    for j,_ in enumerate(m[i]):
        if m[i][j] == "@":
            y_rob = i
            x_rob = j

dir = {
    "<" : (0,-1),
    "v" : (1,0),
    "^" : (-1,0),
    ">" : (0,1)
}

for x in path:
    d = dir[x]
    if m[y_rob + d[1]][x_rob + d[0]] == ".":
        m[y_rob + d[1]][x_rob + d[0]], m[y_rob][x_rob ]  = m[y_rob][x_rob ], m[y_rob + d[1]][x_rob + d[0]]
    elif m[y_rob + d[1]][x_rob + d[0]] == "#":
        pass
    else:
        pass

def res(m):
    s = 0
    for i,_ in enumerate(m):
        for j,_ in enumerate(m[i]):
            if m[i][j] == "O":
                s += 100 * i + j
    return s

s = res(m)
print(f"{s= }")