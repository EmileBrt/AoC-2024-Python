from copy import deepcopy

with open("i2.txt") as f:
    data = f.readlines()

s = 0
for i,d in enumerate(data):
    data[i] = data[i].replace("\n","")
    data[i] = data[i].split(" ")
    for j,x in enumerate(data[i]):
        data[i][j] = int(data[i][j])

for _,d in enumerate(data):
    diff = []
    for i in range(len(d)-1):
        diff.append(d[i+1] - d[i])
    same_sign = all(n >= 0 for n in diff) or all(n <= 0 for n in diff)
    in_range = all(1 <= abs(n) <= 3 for n in diff)
    if same_sign and in_range:
        s += 1
    else:
        for j,_ in enumerate(d):
            c_d = deepcopy(d)
            c_d.pop(j)
            diff = []
            for i in range(len(c_d)-1):
                diff.append(c_d[i+1] - c_d[i])
            same_sign = all(n >= 0 for n in diff) or all(n <= 0 for n in diff)
            in_range = all(1 <= abs(n) <= 3 for n in diff)
            if same_sign and in_range:
                s += 1
                break

        
print(f"{s= }")