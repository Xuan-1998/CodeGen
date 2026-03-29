from math import comb

n = int(input())
m = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
    for j in range(min(i, m[-1]) + 1):
        if j == 0:
            dp[i][j] = 1
        else:
            for k in range(j + 1):
                dp[i][j] += dp[k][j - 1] * comb(i - k, j - k)

print(dp[n][-1] % (10**9 + 7))
