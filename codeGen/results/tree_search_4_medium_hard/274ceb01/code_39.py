import sys

n = int(input())
m = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
        dp[i] = m[0]
    else:
        dp[i] = min(dp[j]) for j in range(i-1) + (m[i - 1] - 1)

print(min(dp))
