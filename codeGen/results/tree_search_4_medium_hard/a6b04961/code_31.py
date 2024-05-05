import sys

n, m = map(int, input().split())
dp = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    dp[max(u, v)] += 1

for i in range(2, n + 1):
    for j in range(i - 1, max(-1, i - 2), -1):
        if dp[j]:
            dp[i] = max(dp[i], dp[j] * (i - j))
        else:
            break

print(max(0, max(dp)))
