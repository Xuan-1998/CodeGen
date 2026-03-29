import sys

n, m, T = map(int, input().split())
dp = [[[0] * (T + 1) for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        w, t = map(int, input().split())
        dp[i][max(j, 0)][min(T, t)] = max(dp[j][max(0, t - w)], dp[i][max(j, 0)][min(T, t)])

k = 0
t = T
for i in range(n, 0, -1):
    if dp[i][t] > k:
        k = dp[i][t]
        print(i)
        t -= 1

print(k)
