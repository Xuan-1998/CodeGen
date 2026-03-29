import math
n = int(input())

dp = [0] * (n + 1)
for i in range(1, n + 1):
    j = int(math.sqrt(i))
    for k in range(j + 1):
        if (j - k ** 2) >= 0:
            dp[i] = min(dp[i], dp[(j - k ** 2)] + 1)

print(dp[n])
