from collections import defaultdict

n = int(input())
graph = defaultdict(list)
in_degree = [0] * (n + 1)

for i in range(2, n + 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

max_in_degree = max(in_degree[1:])
capital_city = in_degree.index(max_in_degree) + 1

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[0][capital_city] = 0

for i in range(1, n + 1):
    for j in graph[i]:
        dp[i][j] = min(dp[i][j], dp[i - 1][i] + 1)

min_edges_to_reverse = float('inf')
ways_to_choose_capital = []
for i in range(n):
    if dp[0][i] < min_edges_to_reverse:
        min_edges_to_reverse = dp[0][i]
        ways_to_choose_capital = [i + 1]

print(min_edges_to_reverse)
print(*ways_to_choose_capital)
