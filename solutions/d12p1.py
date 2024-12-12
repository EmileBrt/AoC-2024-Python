import numpy as np

def read_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    matrix = [list(line.strip()) for line in lines]
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

file_path = 'i12.txt'
matrix = read_matrix(file_path)

s=0
clusters = find_clusters(matrix)
for cluster in clusters:
    perimeter = calculate_perimeter(matrix, cluster)
    area = len(cluster)
    print(f"Cluster: {cluster}, Perimeter: {perimeter}, Area: {area}")
    s += perimeter*area

print(f"{s= }")

