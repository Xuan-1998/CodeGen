import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(1, n):
        for j in range(n):
            if i == 0:
                dp[i][j] = grid[0][j]
            else:
                min_sum = float('inf')
                for k in range(1, j+1):
                    if k != j:  # Ensure the chosen cell is not in the same column
                        min_sum = min(min_sum, dp[i-1][k-1] + grid[i][j])
                dp[i][j] = min_sum
    
    return min(dp[-1][-1])

if __name__ == "__main__":
    grid = []
    for _ in range(int(input())):
        row = list(map(int, input().split()))
        grid.append(row)
    
    print(min_falling_path_sum(grid))
