import numpy as np

with open("i13.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
games = []

delta = 10_000_000_000_000
for i in range(len(data)//4 + 1):
    u = [int(data[4*i].split(": ")[1].split(', ')[0][2:]) , int(data[4*i].split(": ")[1].split(', ')[1][2:])]
    v = [int(data[4*i+1].split(": ")[1].split(', ')[0][2:]) , int(data[4*i+1].split(": ")[1].split(', ')[1][2:])]
    p = [int(data[4*i+2].split(": ")[1].split(', ')[0][2:])  + delta , int(data[4*i+2].split(": ")[1].split(', ')[1][2:]) + delta]
    games.append([np.array([[u[0],v[0]],[u[1],v[1]]]) , np.array(p)])
    

s=0
for g in games:
    A_inv = np.linalg.inv(g[0])
    R = np.matmul(A_inv,g[1])
    print(R)
    i = int(R[0])
    j = int(R[1])
    cond1 = R[0].is_integer() and R[0] >= 0
    cond2 = R[1].is_integer() and R[1] >= 0
    
    if cond1 and cond2:
        s += 3 * i + j
    
print(f"{s= }")