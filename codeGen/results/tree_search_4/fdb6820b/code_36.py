m, N = map(int, input().split())
dp = [[0]*(N+1) for _ in range(m+1)]

for i in range(1, m+1):
    dp[i][0] = 1
    for j in range(1, N+1):
        if j >= arr[i-1]:
            dp[i][j] = (dp[i-1][j] + dp[i][j-arr[i-1]]) % (10**9 + 7)
        else:
            dp[i][j] = dp[i-1][j]

print(sum(dp[m][i] for i in range(N+1)) % (10**9 + 7))
