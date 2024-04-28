k, n = map(int, input().split())
dp = {1: 1}

for i in range(2, n + 1):
    dp[i] = 0
    for j in range(1, i):
        if i % j == 0:
            dp[i] += dp.get(j, 0)

print(dp[n] % 10000007)
