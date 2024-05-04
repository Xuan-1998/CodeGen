dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = 1  # base case: one block with length 1
    for j in range(1, 10):
        if i == 1:
            dp[i][j] = (10**i - 1) // 10**j
        else:
            dp[i][j] = (dp[i-1][0] + dp[i-1][9]) % 998244353
    prefix_sum = [0] * 10
    for i in range(1, n+1):
        for j in range(10):
            prefix_sum[j] += dp[i][j]
    print(*prefix_sum, sep=' ')
