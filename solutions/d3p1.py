import re

with open("i3.txt") as f:
    data = f.read()

print(data)
pattern = r'(mul\(\d+,\d+\))'
list_mul = re.findall(pattern, data, flags=re.DOTALL)
s=0
for i,x in enumerate(list_mul):
    l = int(x.split("(")[1].split(',')[0])
    r = int(x.split("(")[1].split(',')[1][:-1])
    # print(x)
    # print(l)
    # print(r)
    # input()
    s += (l * r)

print(f"{s= }")