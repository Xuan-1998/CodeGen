n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    dp[i][0] = 1
    for j in range(1, n + 1):
        if j < arr[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i - 1][j] + dp[i][j - arr[i - 1]]) % (10**9 + 7)

print(dp[m][n])
