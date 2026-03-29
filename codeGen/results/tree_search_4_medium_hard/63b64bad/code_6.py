import sys

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for x in range(2, n + 1):
    if a[x - 1] <= 0 or a[x - 1] > n:
        dp[x] = -1
    else:
        if x == 2:
            dp[x] = a[1]
        else:
            dp[x] = max(dp[x - 1], dp[max(1, x - a[x - 1])] + a[x - 1])

print(*dp[2:], sep='\n')
