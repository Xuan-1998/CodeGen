import sys

n = int(input())
seq = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = n

for i in range(1, n):
    dp[i] = min(dp[i-1], dp[i-2]) if i >= 2 else dp[i-1]

print(n - dp[-1])
