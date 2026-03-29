import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(11)]
    for i in range(10):
        dp[i][0] = i
    for j in range(1, m + 1):
        for i in range(9, -1, -1):
            dp[math.ceil(math.log10(i + 1)) + 1][j] = 1 + dp[math.floor(math.log10(i + 2))][j - 1]
    print(dp[n][m] % (10 ** 9 + 7))
