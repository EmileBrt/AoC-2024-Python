with open("i8t.txt") as f:
    data = f.readlines()
d_node = {}

for i,d in enumerate(data):
    for j, x in enumerate(d):
        if x not in d_node:
            d_node[x] = [[i,j]]
        else:
            d_node[x].append([i,j])

for k in d_node:
    pairs = []
    for i in range(len(d_node[k])):
        for j in range(i + 1, len(d_node[k])):
            pairs.append((d_node[k][i], d_node[k][j]))
    for i,p in enumerate(pairs):
        n1 = []
        n2 = []

s = 0
for i,d in enumerate(data):
    for j, x in enumerate(d):
        if "#" == x:
            s += 1
if 14 != s:
    print("False")
print(f"{s= }")