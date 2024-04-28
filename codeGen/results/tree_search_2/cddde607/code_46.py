code = '''
def numPathsWithKCoins(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    # Base case: If we're at the bottom right corner and have exactly K coins, there's only one path.
    dp[N - 1][N - 1][K] = 1

    for i in range(N):
        for j in range(N):
            if i < N - 1:
                # If we can move down from this cell, add the number of paths that reach the next row with exactly K coins.
                dp[i + 1][j][K] += dp[i][j][min(K, arr[i][j])]
            if j < N - 1:
                # If we can move right from this cell, add the number of paths that reach the next column with exactly K coins.
                dp[i][j + 1][K] += dp[i][j][min(K, arr[i][j])]

    return sum(sum(dp[i][N - 1]) for i in range(N))
'''

print(code)
