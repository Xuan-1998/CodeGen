import sys

def min_points_required(grid):
    N, M = len(grid), len(grid[0])
    memo = {(0, 0): grid[0][0]}

    for i in range(1, N):
        for j in range(1, M):
            down_path = sum(memo[(i-1, k)] for k in range(j) if k >= 0 and memo[(i-1, k)] > 0)
            right_path = sum(memo[(k, j-1)] for k in range(i) if k >= 0 and memo[(k, j-1)] > 0)
            min_path = min(down_path, right_path) + grid[i][j]
            memo[(i, j)] = min_path

    return memo[(N-1, M-1)]

if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(N)]
    print(min_points_required(grid))
