import sys

n, t = map(int, input().split())
f = float(input())

dp = [[0] * (t + 1) for _ in range(n)]

for i in range(n):
    for j in range(t + 1):
        if i == 0:
            dp[i][j] = int(10**i * f)
        else:
            prev_dp = dp[i-1][j]
            next_dp = dp[i-1][j-1] if j > 0 else 0
            dp[i][j] = max(prev_dp, next_dp + (int(10**(n-i) * f) % 10 == 5 or int(10**(n-i) * f) % 10 > 4))

print(dp[-1][-1])
