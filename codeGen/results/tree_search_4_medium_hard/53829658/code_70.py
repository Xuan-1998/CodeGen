from collections import defaultdict

n = int(input())
graph = defaultdict(list)
in_degree = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

max_in_degree = max(in_degree[1:])
capital_city = in_degree.index(max_in_degree) + 1

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[1][1] = 0

for i in range(2, n + 1):
    if graph[i]:
        for j in graph[i]:
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)

print(min([dp[capital_city][i] for i in range(2, n + 1)]))
print(*sorted(range(2, n + 1)), sep='\n')
