import sys

n = int(input())
a = list(map(int, input().split()))

max_val = max(a)

dp = [[0] * (max_val + 1) for _ in range(n)]

for i in range(n):
    dp[i][0] = (a[i] % 1 == 0) if i == 0 else 0
    for k in range(1, max_val + 1):
        dp[i][k] = (a[i] % k == 0) and ((i == 0 or dp[i-1][min(k-1, k)]) or dp[i-1][k])

print(sum(dp[-1]) % (10**9 + 7))
