import sys

def solve(N, M, grid):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    def f(i, j):
        if i == N and j == M:
            return 0
        elif i < N or j < M:
            return min(f(max(0, i - 1), j), f(i, max(0, j - 1))) + grid[i][j]
        else:
            return sys.maxsize

    for i in range(N + 1):
        for j in range(M + 1):
            dp[i][j] = f(i, j)

    return dp[N][M]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, M, grid))
