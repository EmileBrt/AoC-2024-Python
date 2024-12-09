with open("i9t.txt") as f:
    data = f.read()

data = list(data)
s = 0

def consecutive(d):
    m = data[0]
    for i in range(len(d)):
        if d[i] != m:
            return i

disk_p = [] # [id, len]
max_id = 0
for i,x in enumerate(data):
    if (i % 2) == 0:
        max_id = i//2
        disk_p.append([i//2, int(data[i])])
    else:
        disk_p.append([".", int(data[i])])

# concat
id_done = max_id
while(id_done != 0):

    for i in range(len(disk_p)):
        if disk_p[i][0] == id_done:
            to_pop = i
    p = disk_p.pop(to_pop)
    print(p)
    print(disk_p)
    input()

    for i,_ in enumerate(disk_p):
        if (disk_p[i][0] == ".") and (disk_p[i][1] == p[1]):
            disk_p[i][0] = p[0]
            to_pop = None
            break # break only the for WARNING
        elif (disk_p[i][0] == ".") and (disk_p[i][1] > p[1]):
            disk_p[i][1] -= p[1]
            disk_p.insert(i,p)
            to_pop = None
            break

    if to_pop != None:
        disk_p.insert(to_pop,p)
    id_done -=1

    
print(disk_p)


disk = []
for i,p in enumerate(disk_p):
    for _ in range(p[1]):
        disk.append(p[0])

disk_str = ""
for i in range(len(disk)):
    disk_str += str(disk[i])
print(disk_str)
s = 0

for i in range(len(disk)):
    if disk[i] != ".":
        s += i * disk[i]
if(2858 != s):
    print("error")
print(f"{s= }")