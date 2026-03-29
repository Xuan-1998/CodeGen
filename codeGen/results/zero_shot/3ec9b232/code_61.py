import sys

n = int(input())
M = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n):
    if M[i-1] < M[i]:
        dp[i] = (dp[i-1] * (2 * i)) % (10**9 + 7)
    else:
        dp[i] = (dp[i-1] * (i+1)) % (10**9 + 7)

print(dp[n]% (10**9 + 7))
