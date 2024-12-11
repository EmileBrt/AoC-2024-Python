import math

with open("i11.txt") as f:
    raw = f.read()
raw = [int(x) for x in raw.split(" ")]

data = {}
for x in raw:
    data[x] = 1

def step_data(data):
    n_d = {}
    for x in data:
        if x == 0:
            if 1 not in n_d:
                n_d[1] = data[x]
            else:
                n_d[1] += data[x]
        elif math.floor(math.log10(x)) % 2 == 1:
            n1 = int(str(x)[:len(str(x))//2])
            n2 = int(str(x)[len(str(x))//2:])
            if n1 not in n_d:
                n_d[n1] = data[x]
            else:
                n_d[n1] += data[x]

            if n2 not in n_d:
                n_d[n2] = data[x]
            else:
                n_d[n2] += data[x]
        else:
            n = 2024 * x 
            if n not in n_d:
                n_d[n] = data[x]
            else:
                n_d[n] += data[x]
    return n_d

for i in range(75):
    print(f"DONE : {100 * i / 75}")
    data = step_data(data)
    
s = 0
for k in data:
    s += data[k]
print(f"{s= }")

