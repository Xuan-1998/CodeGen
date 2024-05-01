from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
fixed_path = list(map(int, input().split()))
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def dfs(i, j):
    if i == fixed_path[-1]:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    dp = float('inf')
    for neighbor in graph[i]:
        if neighbor not in fixed_path:
            dp = min(dp, dfs(neighbor, j) + 1)
    memo[i][j] = min(dp, 0)
    return memo[i][j]

memo = [[-1] * (n + 1) for _ in range(n + 1)]
print(dfs(fixed_path[0], 0), dfs(fixed_path[-2], 0))
