n = int(input())
dp = [[0] * 4 for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = 20
for i in range(1, n + 1):
    for j in range(min(i-1, 3) + 1):
        if j == i - 1:
            dp[i][j] = dp[i-1][j]
        else:
            one_trip = dp[i-1][j]
            ninety_minutes = dp[i-j-1][j] + 50
            one_day = dp[i-1440][j] + 120
            dp[i][j] = min(one_trip, ninety_minutes, one_day)
print(dp[n][0])
