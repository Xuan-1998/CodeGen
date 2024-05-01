import sys

def min_falling_path_sum(grid):
    R = len(grid)
    C = len(grid[0])
    
    dp = [[0] * C for _ in range(R)]
    
    # Base case: Initialize the first row
    for j in range(C):
        dp[0][j] = grid[0][j]
    
    for i in range(1, R):
        for j in range(C):
            min_sum = sys.maxsize
            for k in range(C):
                if abs(k - j) != 1:  # Check if column k is not adjacent to column j
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum
    
    return min(dp[-1])

if __name__ == "__main__":
    grid = [[2, 5, 3], [8, 6, 9], [4, 7, 10]]
    print(min_falling_path_sum(grid))
