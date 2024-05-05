def count_stable_tables():
    N, M = map(int, input().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # Base case: single row
    for j in range(M + 1):
        dp[0][j] = M + 1

    for i in range(1, N + 1):
        for j in range(M, -1, -1):
            if j >= M - (N - i):
                dp[i][j] = dp[i-1][M - (N - i)]
            else:
                dp[i][j] = min(dp[i-1][k] for k in range(j+1)) + 1

    # Calculate the result
    total = sum(1 for row in dp[-1]):
        return total % (10**9 + 7)

print(count_stable_tables())
