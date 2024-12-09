with open("i9.txt") as f:
    data = f.read()

data = list(data)
disk_p = []
max_id = 0

for i,x in enumerate(data):
    if x != "0":
        if (i % 2) == 0:
            max_id = i//2
            disk_p.append([i//2, int(data[i])])
        else:
            disk_p.append([".", int(data[i])])

def is_concat(disk_p):
    for i in range(len(disk_p)-1):
        if disk_p[i][0] == disk_p[i + 1][0]:
            return i
    return -1

def concat(disk_p):
    while(is_concat(disk_p) > 0):
        i = is_concat(disk_p)
        disk_p[i][1] += disk_p[i+1][1]
        disk_p.pop(i+1)
    return disk_p
def print_disk(disk_p):
    s = ""
    for i,p in enumerate(disk_p):
        for _ in range(p[1]):
            s += str(p[0])
    return s
mm = max_id
while(max_id != 0):
    if max_id % 100 == 0:
        print(f"DONC {round(100 * max_id / mm)} % ")
    disk_p = concat(disk_p)
    for i,p in enumerate(disk_p):
        if p[0] == max_id:
            index = i
    swapped = False
    for i,p in enumerate(disk_p):
        if p[0] == "." and i < index and p[1]:
            if p[1] == disk_p[index][1]:
                disk_p[index] , disk_p[i] =disk_p[i] , disk_p[index]
                break
            elif p[1] > disk_p[index][1]:
                r = p[1] - disk_p[index][1]
                disk_p[i][1] = disk_p[index][1]
                disk_p[index] , disk_p[i] =disk_p[i] , disk_p[index]
                disk_p.insert(i+1,[".",r])
                break    
    max_id -= 1
print("res")
print_disk(disk_p)
print("00992111777.44.333....5555.6666.....8888..")

s = 0
c = 0
for i,p in enumerate(disk_p):
    for i in range(c, c + p[1]):
        if p[0] != ".":
            s += i * p[0]
    c += p[1]

print(f"{s= }")