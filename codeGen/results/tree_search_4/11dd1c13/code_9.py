from collections import deque

def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0] = grid[0]
    
    queue = deque([(i, j) for i in range(m) for j in range(n)])
    
    while queue:
        i, j = queue.popleft()
        
        if i > 0:
            for k in range(max(0, j - 1), min(n, j + 2)):
                if abs(j - k) != 1:  # non-adjacent columns
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i][j])
    
    return min(dp[-1])

# Read the grid from stdin and print the result to stdout.
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
