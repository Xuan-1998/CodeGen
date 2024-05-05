import sys

n = int(input())
p = list(map(int, input().split()))

dp = [-sys.maxsize] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    if dp[i - 1] == -sys.maxsize:
        continue
    dp[i] = min(dp[i-1], dp[p[i - 1] - 1])
    if (i % 2 != 0 and dp[i] == dp[i-1]) or (i % 2 == 0 and dp[i] == dp[p[i - 1] - 1]):
        dp[i] += 1

print(dp[n] % (10**9 + 7))
