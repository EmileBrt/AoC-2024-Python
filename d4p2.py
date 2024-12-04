with open("i4.txt") as f :
    data = f.readlines()

A_ind = []

for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        if data[i][j] == "A":
            A_ind.append([i,j])
s=0

for i,x in A_ind:
    if( ( data[A_ind[i][0]-1][A_ind[i][1]-1] != data[A_ind[i][0]+1][A_ind[i][1]+1] ) and ( data[A_ind[i][0]+1][A_ind[i][1]-1] != data[A_ind[i][0]-1][A_ind[i][1]+1] )):
        s+=1
print(f"{s= }")