import sys

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

dp = [0] * (n + 1)
tail = [0] * (n + 1)

for u, v in edges:
    for i in range(n + 1):
        if dp[i] < dp[i - 1] + 1 and tail[v] > tail[i]:
            dp[i] = dp[i - 1] + 1
            tail[i] = tail[v]
        elif dp[i] < tail[i - 1] + 1:
            dp[i] = tail[i - 1] + 1

print(max(dp))
