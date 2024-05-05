import sys

def min_initial_points(points):
    N, M = len(points), len(points[0])
    dp = [[0] * M for _ in range(N)]

    # Initialize base cases
    for j in range(M):
        dp[0][j] = points[0][j]
    for i in range(N):
        dp[i][0] = points[i][0]

    # Fill up the dp array
    for i in range(1, N):
        for j in range(1, M):
            if points[i-1][j] > 0:
                right_move = min(dp[i-1][j], dp[i][j-1]) + 1
                down_move = min(dp[i-1][j-1], dp[i][j-1]) + 1
                dp[i][j] = min(right_move, down_move)

    return dp[N-1][M-1]

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
points = [[int(x) for x in line.split()] for line in sys.stdin.read().strip().splitlines()]

# Print the answer to stdout
print(min_initial_points(points))
