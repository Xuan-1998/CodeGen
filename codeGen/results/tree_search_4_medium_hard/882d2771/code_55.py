import sys

t, l, r = map(int, input().split())

dp = [[0] * 2 for _ in range(50007)]

for i in range(3):
    dp[i][1] = i - 1

for n in range(4, r + 1):
    if n % 2 == 0:
        dp[n][0] = min(dp[i][1] + 1 for i in range(n-1, 2, -2)) + (n//2 - 1)
        dp[n][1] = min(min(dp[i][0], dp[j][1]) + n//2 - 1 for j in range(n, 2, -2) for i in range(j))
    else:
        dp[n][0] = min(dp[i][1] + 1 for i in range(n-1, 3, -2)) + (n//2)
        dp[n][1] = min(min(dp[i][0], dp[j][1]) + n//2 for j in range(n, 3, -2) for i in range(j))

print((dp[r][0] * t0 + dp[r][1] * t1 - l * dp[r][0]) % (10**9 + 7))
