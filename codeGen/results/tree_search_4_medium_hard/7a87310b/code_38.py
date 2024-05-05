dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    dp[i][0] = 0
    if i > 0:
        dp[i][i] = 1

for N in range(3, max_val+1):
    for j in range(1, N+1):
        # Calculate the determinant for each possible combination of elements
        for k in range(N//2+1):
            if (N - 2*k) % 2 == 0:
                dp[N][j] += dp[N-2*k][k]

print(dp[max_val][max_val])
