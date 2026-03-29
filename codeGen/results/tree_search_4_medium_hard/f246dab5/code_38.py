n = int(input())
dp = [[[float('inf')] * 90] * (n + 1)] * 2

for i in range(1, n + 1):
    for k in range(n // 90 + 1):
        dp[0][k][i % 90] = min(dp[0][k][i % 90], 
                                dp[0][k - 1][((i - 1) % 90)] + 50, 
                                dp[0][0][i % 90] + 20)
        if k > 0 and (i % 90 != i // 90 or k == 1):
            dp[1][k - 1][i % 90] = min(dp[1][k - 1][i % 90], 
                                        dp[0][k - 1][((i - 1) % 90)] + 50, 
                                        dp[0][0][i % 90] + 20)

for i in range(1, n + 1):
    for k in range(n // 90 + 1):
        print(dp[1][k][i % 90])
