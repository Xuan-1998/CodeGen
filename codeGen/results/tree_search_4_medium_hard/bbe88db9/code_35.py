import sys

n = int(input())
p = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n + 1):
    if p[i - 1] % 2 == 0:
        dp[i] = min(dp[k] for k in range(i)) + 1
    else:
        dp[i] = min(dp[k] + 1 for k in range(i))

print(dp[-1] % (10**9 + 7))
