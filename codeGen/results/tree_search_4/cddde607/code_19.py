from itertools import product

def count_paths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i, j in product(range(N), range(N)):
        if i == 0 and j == 0:
            dp[i][j][arr[i][j]] = 1
        elif i > 0:
            dp[i][j][k] += dp[i-1][j][max(0, k - arr[i][j])]
        elif j > 0:
            dp[i][j][k] += dp[i][j-1][max(0, k - arr[i][j])]

    return dp[N-1][N-1][K]
