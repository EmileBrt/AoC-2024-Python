with open("i4.txt") as f :
    data = f.readlines()

# data = [
# "MMMSXXMASM",
# "MSAMXMSMSA",
# "AMXSXMAAMM",
# "MSAMASMSMX",
# "XMASAMXAMM",
# "XXAMMXXAMA",
# "SMSMSASXSS",
# "SAXAMASAAA",
# "MAMMMXMMMM",
# "MXMXAXMASX"
# ]
A_ind = []

r = ["MS","SM"]
s = 0
for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        if data[i][j] == "A":
            A_ind.append([i,j])
            lft = data[i+1][j+1]+data[i-1][j-1]
            rgt = data[i-1][j+1]+data[i+1][j-1]
            if (lft in r) and (rgt in r):
                s += 1

print(f"{s= }")