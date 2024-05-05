import sys

def min_initial_points(N, M, grid):
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N+1):
        for j in range(M+1):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            elif i > 0:
                if j > 0 and grid[i-1][j-1] > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            elif j > 0:
                if grid[0][j-1] > 0:
                    dp[i][j] = min(dp[i][j-1]) + 1
                else:
                    dp[i][j] = max(dp[i][j-1])

    return dp[N][M]

# Example usage
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
print(min_initial_points(N, M, grid))
