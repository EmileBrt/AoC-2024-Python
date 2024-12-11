import math

with open("i11.txt") as f:
    data = f.read()
data = [int(x) for x in data.split(" ")]

def step_data(data):
    n_d = []
    for x in data:
        if x == 0:
            n_d.append(1)
        elif math.floor(math.log10(x)) % 2 == 1:
            n_d.append(int(str(x)[:len(str(x))//2]))
            n_d.append(int(str(x)[len(str(x))//2:]))
        else:
            n_d.append(2024 * x)
    return n_d

for _ in range(25):
    data = step_data(data)

s = len(data)
print(f"{s= }")

