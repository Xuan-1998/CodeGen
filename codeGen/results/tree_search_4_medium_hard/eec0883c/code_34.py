import sys

def solve(n, w, edges):
    memo = {}

    def dfs(city, remaining_gasoline):
        if (city, remaining_gasoline) in memo:
            return memo[(city, remaining_gasoline)]
        
        max_gasoline = 0
        for neighbor, c in edges[city]:
            new_gasoline = min(w[neighbor], w[city] - c + remaining_gasoline)
            max_gasoline = max(max_gasoline, dfs(neighbor, new_gasoline))
        
        memo[(city, remaining_gasoline)] = max_gasoline
        return max_gasoline

    for i in range(n):
        if not edges[i]:
            return w[i]

    return dfs(0, 0)

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
edges = [[] for _ in range(n)]

for _ in range(n-1):
    u, v, c = map(int, sys.stdin.readline().split())
    edges[u].append((v, c))
    edges[v].append((u, c))

print(solve(n, w, edges))
