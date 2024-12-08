with open("i2.txt") as f:
    data = f.readlines()

s = 0
for i,d in enumerate(data):
    data[i] = data[i].replace("\n","")
    data[i] = data[i].split(" ")
    for j,x in enumerate(data[i]):
        data[i][j] = int(data[i][j])

for i,d in enumerate(data):
    diff = []
    for i in range(len(d)-1):
        diff.append(d[i+1] - d[i])
    same_sign = all(n >= 0 for n in diff) or all(n <= 0 for n in diff)
    in_range = all(1 <= abs(n) <= 3 for n in diff)
    if same_sign and in_range:
        s += 1
print(f"{s= }")