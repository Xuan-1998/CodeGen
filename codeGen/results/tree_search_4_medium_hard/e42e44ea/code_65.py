import heapq

def minInitialPoints(N, M, grid):
    # Initialize DP table
    dp = [[0] * M for _ in range(N)]

    # Prioritize cells with maximum positive points
    pq = [(grid[0][0], 0, 0)]  # (points, i, j)
    heapq.heapify(pq)

    while pq:
        points, i, j = heapq.heappop(pq)
        if i < N - 1 and dp[i + 1][j] == 0:  # Down
            new_points = points + grid[i + 1][j]
            heapq.heappush(pq, (new_points, i + 1, j))
        if j < M - 1 and dp[i][j + 1] == 0:  # Right
            new_points = points + grid[i][j + 1]
            heapq.heappush(pq, (new_points, i, j + 1))

    return dp[N - 1][M - 1]

# Example usage:
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
print(minInitialPoints(N, M, grid))
