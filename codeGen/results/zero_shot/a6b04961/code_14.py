import sys

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

edges.sort()

dp = [[False] * (n + 1) for _ in range(n + 1)]
ans = 0
tail_len = 0

for i in range(2, n + 1):
    for j in range(i):
        if not dp[j][i - 1]:
            tail_len += 1
            ans = max(ans, tail_len * (n - i))
            dp[j][i] = True

print(ans)
