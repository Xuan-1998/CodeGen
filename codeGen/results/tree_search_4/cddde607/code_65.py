import sys

def coinPaths(K, N, arr):
    dp = [[[0] * (K + 1) for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = 1
            elif i > 0 or j > 0:
                if arr[i][j] <= K:
                    dp[i][j][arr[i][j]] = (dp[i-1][j][arr[i][j]-arr[i][j]] + 
                                             dp[i][j-1][arr[i][j]-arr[i][j]]) if i > 0 and j > 0 else \
                                             dp[(i-1 if i > 0 else N-1)][j][arr[i][j]-arr[i][j]] + \
                                             dp[i][(j-1 if j > 0 else N-1)][arr[i][j]-arr[i][j]]
                else:
                    dp[i][j][K] = 0

    return dp[N-1][N-1][K]

# Test cases
K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(coinPaths(K, N, arr))
