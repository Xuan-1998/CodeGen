from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for i in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[float('inf')] * (n+1) for _ in range(n+1)]
dp[1][0] = 1

for p in range(1, n):
    for i in range(p+1):
        if i:
            dp[i][p] = min(dp[j][p-1] + (i != j) for j in graph[i])
        else:
            dp[i][p] = p
        if not dp[i][p]:
            break
print(min(dp[-1]))
