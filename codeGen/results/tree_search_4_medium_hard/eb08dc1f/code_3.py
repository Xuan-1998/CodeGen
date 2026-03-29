===BEGIN CODE===
n = int(input())

dp = [[0] * (n + 1) for _ in range(10)]

for i in range(10):
    dp[i][1] = 1

for j in range(2, n + 1):
    for k in range(10):
        if j > 1:
            for prev in range(10):
                dp[k][j] += (dp[prev][j - 1] % 998244353)
        else:
            dp[k][j] = 1

res = [0] * n
for i in range(10):
    res[i] = sum([dp[i][j] for j in range(n + 1)]) % 998244353

print(*res, sep=' ')
===END CODE===
