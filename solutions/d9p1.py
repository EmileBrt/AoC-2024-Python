with open("i9.txt") as f:
    data = f.read()
data = list(data)
print(data)
s = 0
disk = []
for i,x in enumerate(data):
    if (i % 2) == 0:
        for _ in range(int(data[i])):
            disk.append(i//2)
    else:
        for _ in range(int(data[i])):
            disk.append(".")
## concat
while("." in disk):
    m = disk.pop()
    while(m == "."):
        m = disk.pop()
    for i in range(len(disk)):
        if "." == disk[i]:
            disk[i] = m
            break

id_part = []
s = 0
for i in range(len(disk)):
    s += i * disk[i]
print(f"{s= }")