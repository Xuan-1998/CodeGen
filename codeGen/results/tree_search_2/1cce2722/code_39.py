import sys

n = int(input())
sequence = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    k = max(j for j in range(i) if sequence[j] <= sequence[i])
    dp[i + 1] = min(dp[k - 2:i], default=1) + (i >= k - 2)

print(max(0, *dp))
