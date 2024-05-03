import sys

n, m = map(int, input().split())
dp = [[sys.maxsize for _ in range(m)] for _ in range(n + 1)]

for i in range(1, n + 1):
    s, x = map(int, input().split())
    dp[i][s - 1] = min(dp[i][s - 1], dp[i - 1][s])

print(min(dp[n]))
