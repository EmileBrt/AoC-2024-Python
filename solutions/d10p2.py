import networkx as nx

with open("i10.txt") as f:
    data = f.readlines()

G = nx.DiGraph()

dir = [(1,0), (-1,0), (0,-1),(0,1)]
for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")
    data[i] = [ int(x) for x in list(data[i]) ]
    data[i].append(-9)
    data[i].insert(0,-9)

data.append([-9 for _ in range(len(data[0]))])
data.insert(0,[-9 for _ in range(len(data[0]))])

print(data[0])
print(data[1])

n = len(data[0])

i9 = []
i0 = []

# Create Every Node
for i,_ in enumerate(data):
    for j,_ in enumerate(data[i]):
        G.add_node(str([i,j]))
        if data[i][j] == 0:
            i0.append([i,j])
        elif data[i][j] == 9:
            i9.append([i,j])


# Create Every Edge
for i in range(1, len(data) - 1 ):
    for j in range(1, len(data[0]) - 1):
        for d in dir:
            if ( data[i + d[0]][j + d[1]] - data[i][j] ) == 1:
                G.add_edge(str([i,j]) ,str([i + d[0],j + d[1]]))


res = 0
for _,s in enumerate(i0):
    for _,e in enumerate(i9):
        res += len(list(nx.all_simple_paths(G, str(s), str(e))))

print(f"{res= }")