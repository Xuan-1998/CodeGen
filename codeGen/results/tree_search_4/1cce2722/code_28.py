import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * n
for i in range(n):
    dp[i] = max(dp[k] + (k-i) + (n-k) - (a[i]-a[k]) for k in range(i)) if i > 0 else 0

print(max(dp))
