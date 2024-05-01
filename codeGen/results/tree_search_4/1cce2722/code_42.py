import sys

n = int(input())
a = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(2, n):
    dp[i] = dp[i - 1]
    for j in range(i - 2, -1, -1):
        if a[j] == a[i]:
            dp[i] = max(dp[i], dp[j] + (i - j))
            break

print(max(0, dp[-1]))
