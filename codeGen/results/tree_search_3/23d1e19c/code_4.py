import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
recommended_path = list(map(int, input().split()))
min_val = sys.maxsize
max_val = 0

dp = [[sys.maxsize] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    if recommended_path[0] == i:
        dp[i][0] = 0
    else:
        dp[i][0] = 1

for j in range(1, k + 1):
    for i in range(1, n + 1):
        if i == recommended_path[j]:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1]) if i > 0 else 0
        elif graph[i]:
            dp[i][j] = min(1 + min(dp[v][j] for v in graph[i]), dp[i][j - 1])
        else:
            dp[i][j] = dp[i][j - 1]

for j in range(1, k + 1):
    min_val = min(min_val, min(dp[i][j] for i in range(n + 1)))
    max_val = max(max_val, max(dp[i][j] for i in range(n + 1)))

print(min_val)
print(max_val)
