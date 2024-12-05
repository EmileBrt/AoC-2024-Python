import json

with open("i5.txt") as f:
    data = f.readlines()

rules = data[:1176]
pages = data[1177:]

dico = {}

for i,x in enumerate(rules):
    rules[i] = [ int(x) for x in rules[i].replace("\n","").split("|") ]

    if rules[i][0] not in dico:
        dico.update({rules[i][0]:{
            "l":[],
            "r":[]
        }})
    if rules[i][1] not in dico:
        dico.update({rules[i][1]:{
            "l":[],
            "r":[]
        }})
    dico[rules[i][0]]["r"].append(rules[i][1])
    dico[rules[i][1]]["l"].append(rules[i][0])

s=0
for i,x in enumerate(pages):
    pages[i] = [ int(k) for k in pages[i].replace("\n","").split(",")]
    is_ordered = True
    print(pages[i])
    for j,y in enumerate(pages[i]):
        #l_cond = all(elem in pages[i][:j]  for elem in dico[y]["l"])FUCK YOU CHATGPT
        l_cond = set(pages[i][:j]).issubset(set(dico[y]["l"]))
        #r_cond = all(elem in pages[i][j+1:] for elem in dico[y]["r"]) FUCK YOU CHATGPT
        r_cond = set(pages[i][j+1:]).issubset(set(dico[y]["r"]))
        if j == 0:
            l_cond = True
        if j == len(pages[i])-1:
            r_cond = True
        if False == l_cond or False == r_cond:
            is_ordered = False
        print(f"{l_cond=}")
        print(f"{r_cond=}")
        print(f"{pages[i][:j]=}")
        print(f"{pages[i][j+1:]=}")
        #input()
    if is_ordered == True:
        s += pages[i][(len(pages[i]) - 1) // 2]

print(f"{s= }")