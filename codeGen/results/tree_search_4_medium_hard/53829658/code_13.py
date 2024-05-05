from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)

dp = [[False] * (n+1) for _ in range(n)]

for i in range(1, n+1):
    dp[i][0] = True

for k in range(1, n+1):
    for i in range(1, n+1):
        if not dp[i][k-1]:
            continue
        for j in graph[i]:
            dp[j][k] = True

capital_cities = [i for i in range(1, n+1) if all(dp[i][k]) for k in range(n)]
min_reversed_edges = min(k for i, k in enumerate(capital_cities) if not dp[capital_cities[i]][k-1])
print(min_reversed_edges)
print(*capital_cities, sep='\n')
