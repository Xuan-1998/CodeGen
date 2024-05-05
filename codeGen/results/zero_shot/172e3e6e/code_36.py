import sys

# read input
n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n):
    for j in range(i, -1, -1):
        if a[j-1] % j == 0:
            dp[i] += dp[j-1]
        if i > 0 and a[i] % (i+1) == 0:
            dp[i] += dp[i-1]

print(dp[-1]%10**9+7)
