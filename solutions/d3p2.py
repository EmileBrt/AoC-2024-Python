import re

with open("i3.txt") as f:
    data = f.read()

print(data)
pattern_mul = r'(mul\(\d+,\d+\))'
matches_mul_str = [(match.group(), match.start()) for match in re.finditer(pattern_mul, data, flags=re.IGNORECASE)]
mul_index = []
mul_str = []
for i,x in enumerate(matches_mul_str):
    mul_str.append(x[0])
    mul_index.append(x[1])
pattern_do = r'(do\(\))'
do_index = [ (match.group(), match.start())  for match in re.finditer(pattern_do, data, flags=re.IGNORECASE)]
for i,_ in enumerate(do_index):
    do_index[i] = do_index[i][1]

pattern_dont = r'(don\'t\(\))'
dont_index = [ (match.group(), match.start())  for match in re.finditer(pattern_dont, data, flags=re.IGNORECASE)]
for i,_ in enumerate(dont_index):
    dont_index[i] = dont_index[i][1]

s=0
state = True

for i,_ in enumerate(data):
    if i in do_index:
        state = True
    if i in dont_index:
        state = False
    if i in mul_index and state == True:
        j = mul_index.index(i)
        x = mul_str[j]
        l = int(x.split("(")[1].split(',')[0])
        r = int(x.split("(")[1].split(',')[1][:-1])
        s += (l * r)
print(f"{s= }")