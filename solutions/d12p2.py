import numpy as np

def read_color_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove any trailing newlines and convert each line to a list of characters
    matrix = [list(line.strip()) for line in lines]

    # Convert the list of lists to a numpy array
    np_matrix = np.array(matrix)
    return np_matrix

def find_clusters(matrix):
    rows, cols = matrix.shape
    visited = np.zeros((rows, cols), dtype=bool)
    clusters = []

    def dfs(x, y, color):
        stack = [(x, y)]
        cluster = []
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) not in cluster:
                cluster.append((cx, cy))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx, ny] and matrix[nx, ny] == color:
                    visited[nx, ny] = True
                    stack.append((nx, ny))
        return cluster

    for i in range(rows):
        for j in range(cols):
            if not visited[i, j]:
                visited[i, j] = True
                cluster = dfs(i, j, matrix[i, j])
                clusters.append(cluster)

    return clusters

def calculate_perimeter(matrix, cluster):
    rows, cols = matrix.shape
    perimeter = 0
    for x, y in cluster:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or matrix[nx, ny] != matrix[x, y]:
                perimeter += 1
    return perimeter

def count_unique_sides(matrix, cluster):
    rows, cols = matrix.shape
    unique_sides = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in cluster:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < rows and 0 <= ny < cols) or matrix[nx, ny] != matrix[x, y]:
                unique_sides.add((x, y, dx, dy))

    return len(unique_sides)



file_path = 'i12t.txt'
matrix = read_color_matrix(file_path)

s=0
clusters = find_clusters(matrix)
for cluster in clusters:
    angles = count_unique_sides(matrix, cluster)
    area = len(cluster)
    print(f"Cluster: {cluster}, Sides: {angles}, Area: {area}")
    s += angles*area

print(f"{s= }")