# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
import functools
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

