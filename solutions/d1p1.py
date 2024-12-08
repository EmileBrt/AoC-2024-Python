with open("i1.txt") as f:
    data = f.readlines()
l, r = [],[]
for i,_ in enumerate(data):
    data[i] = data[i].replace("\n","")
    l.append(int(data[i].split(" ")[0]))
    r.append(int(data[i].split(" ")[-1]))

l.sort()
r.sort()
s = 0
for i,_ in enumerate(l):
    s += abs(r[i] - l[i])

print(f"{s= }")