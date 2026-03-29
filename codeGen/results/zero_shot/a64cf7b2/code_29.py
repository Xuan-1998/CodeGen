def dfs(i, t):
    global max_vertices, path
    if i > n or t > T:
        return
    if visited[i]:
        return
    visited[i] = True
    path.append(i)
    for u, v, edge_t in edges:
        if u == i and not visited[v]:
            dfs(v, t + edge_t)
    if len(path) > max_vertices:
        max_vertices = len(path)
    path.pop()

def main():
    global n, m, T
    n = int(input())
    m = int(input())
    T = int(input())
    edges = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        edges.append((u, v, t))
    
    visited = [False] * (n + 1)
    max_vertices = 0
    path = []
    dfs(1, 0)
    print(max_vertices)
    for i in range(max_vertices):
        print(path[i])
