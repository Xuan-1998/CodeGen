import sys

def find_center(graph):
    # Calculate the MST using Kruskal's algorithm
    mst = []
    edges = [(u, v) for u in range(1, n+1) for v in range(u+1, n+1)]
    edges.sort(key=lambda x: graph[x[0]-1][x[1]-1])
    parent = list(range(n+1))
    rank = [0] * (n+1)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
    for edge in edges:
        u, v = edge
        if find(u) != find(v):
            mst.append(edge)
            union(u, v)
    # Calculate the average distance from each city to all other cities
    avg_distances = [0] * (n+1)
    for i in range(n+1):
        for j in range(i+1, n+1):
            if graph[i-1][j-1]:
                avg_distances[i] += 1
                avg_distances[j] += 1
    # Find the city with the minimum average distance
    min_avg_distance = float('inf')
    center = None
    for i in range(1, n+1):
        if avg_distances[i] < min_avg_distance:
            min_avg_distance = avg_distances[i]
            center = i
    return center

n = int(sys.stdin.readline())
graph = [list(map(int, line.strip().split())) for line in sys.stdin.readlines()[1:]]
center = find_center(graph)
print(min_avg_distance)  # Minimum number of roads to be reversed
print(center)  # Index of the chosen capital city
