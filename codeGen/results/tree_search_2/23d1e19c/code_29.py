import sys

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
                if rank[root_x] == rank[root_y]:
                    rank[root_y] += 1
    
    for edge in edges:
        union(edge[0], edge[1])
    
    path_components = set()
    for i in range(k - 1):
        path_components.add(find(path[i]))
    
    dp = [[0, 0]] * n
    for p in path:
        if find(p) != find(t):
            dp[p] = [min(dp[path.index(p)][0], 1 + dp[path.index(path[path.index(p) + 1])][0]), 
                     max(dp[path.index(p)][1], 1 + dp[path.index(path[path.index(p) + 1])][1])]
        else:
            dp[p] = [0, 0]
    
    print(min(max(dp[i][0] for i in range(n)), key=lambda x: (x[0], -x[1])))
