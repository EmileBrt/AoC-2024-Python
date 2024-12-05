import json
from functools import cmp_to_key

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


def compare(a,b):
  if a in dico[b]["l"]: return -1
  if a in dico[b]["r"]: return 1
  if b in dico[b]["l"]: return -1
  if b in dico[b]["r"]: return 1
  return 0

s=0
for i,x in enumerate(pages):
    pages[i] = [ int(k) for k in pages[i].replace("\n","").split(",")]
    is_ordered = True
    for j,y in enumerate(pages[i]):
        l_cond = set(pages[i][:j]).issubset(set(dico[y]["l"]))
        r_cond = set(pages[i][j+1:]).issubset(set(dico[y]["r"]))
        if j == 0:
            l_cond = True
        if j == len(pages[i])-1:
            r_cond = True
        if False == l_cond or False == r_cond:
            is_ordered = False
    if is_ordered == False:
        ordered = sorted(pages[i],key=cmp_to_key(compare))
        s += ordered[(len(ordered) - 1) // 2]

print(f"{s= }")