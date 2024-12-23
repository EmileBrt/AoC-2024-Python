with open("i8.txt") as f:
    data = f.readlines()

for i,d in enumerate(data):
    data[i] = d.replace("\n","")
    data[i] = list(data[i])

d_node = {}

for i,d in enumerate(data):
    for j, x in enumerate(d):
        if x != '.':
            if x not in d_node:
                d_node[x] = [[i,j]]
            else:
                d_node[x].append([i,j])

s = 0

antinodes = []
for k in d_node:
    pairs = []
    for i in range(len(d_node[k])):
        for j in range(i + 1, len(d_node[k])):
            pairs.append((d_node[k][i], d_node[k][j]))
    for i,p in enumerate(pairs):
        n1 = [ p[1][0] + (p[1][0] - p[0][0]) , p[1][1] + (p[1][1] - p[0][1])]
        n2 = [ p[0][0] - (p[1][0] - p[0][0]) , p[0][1] - (p[1][1] - p[0][1])]
        n = [n1,n2]

        for m in n:
            if  (0 <= m[0] < len(data)) and (0 <= m[1] < len(data[0])):
                if m not in antinodes:
                    antinodes.append(m)
s = len(antinodes)
print(f"{s= }")