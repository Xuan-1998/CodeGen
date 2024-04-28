dp = [[[False] * (K + 1)] * N] * N

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:  # base case
            dp[i][j][arr[i][j]] = True
        elif i > 0:
            dp[i][j] = [dp[i-1][j] or (i < N-1 and dp[i-1][j] and arr[i-1][j] + K >= arr[i][j]) for _ in range(K+1)]
        elif j > 0:
            dp[i][j] = [dp[i][j-1] or (j < N-1 and dp[i][j-1] and arr[i][j-1] + K >= arr[i][j]) for _ in range(K+1)]

result = sum([all(dp[N-1][N-1][k]) for k in range(K+1)])
