import re

with open("i4.txt") as f :
    data = f.readlines()

line = data
transposed = ["".join([row[i] for row in data]) for i in range(len(data[0]))]

def extract_diagonals(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Collect diagonals (-45°)
    diagonals_45 = []
    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                diagonal.append(grid[i][j])
        if diagonal:
            diagonals_45.append("".join(diagonal))

    # Collect anti-diagonals (45°)
    diagonals_minus45 = []
    for d in range(rows + cols - 1):
        anti_diagonal = []
        for i in range(rows):
            j = i + d - (cols - 1)
            if 0 <= j < cols:
                anti_diagonal.append(grid[i][j])
        if anti_diagonal:
            diagonals_minus45.append("".join(anti_diagonal))

    return diagonals_45, diagonals_minus45

diag1 , diag2 = extract_diagonals(data)
print(line[0])
print(transposed[0])
for i in range(len(diag2)):
    print(diag2[i])

res = [j for i in [line, transposed, diag1,diag2] for j in i]
s = 0
pattern = r"(?=(XMAS|SAMX))"
for i,x in enumerate(res):
    matches_mul_str = [(match.group(), match.start()) for match in re.finditer(pattern, x, flags=re.IGNORECASE)]
    s += len(matches_mul_str)

print(f"{s= }")
