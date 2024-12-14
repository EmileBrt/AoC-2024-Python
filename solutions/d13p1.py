import numpy as np

with open("i13.txt") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("\n","")
games = []
for i in range(len(data)//4 + 1):
    u = [int(data[4*i].split(": ")[1].split(', ')[0][2:]) , int(data[4*i].split(": ")[1].split(', ')[1][2:])]
    v = [int(data[4*i+1].split(": ")[1].split(', ')[0][2:]) , int(data[4*i+1].split(": ")[1].split(', ')[1][2:])]
    p = [int(data[4*i+2].split(": ")[1].split(', ')[0][2:]) , int(data[4*i+2].split(": ")[1].split(', ')[1][2:])]
    games.append([np.array([[u[0],v[0]],[u[1],v[1]]]) , np.array(p)])
    

s=0
for g in games:
    A_inv = np.linalg.inv(g[0])
    R = np.matmul(A_inv,g[1])
    print(R)
    i = int(round(R[0]))
    j = int(round(R[1]))
    epsilon = 0.01
    cond1 = abs(R[0] - round(R[0])) < epsilon
    cond2 = abs(R[1] - round(R[1])) < epsilon
    
    if cond1 and cond2 :
        s += 3 * i + j
    

print(f"{s= }")