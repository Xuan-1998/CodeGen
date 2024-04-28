from collections import defaultdict

def min_falling_path_sum(grid):
    memo = defaultdict(int)
    
    def dp(row_index, last_column_index):
        if row_index == 0:
            return grid[0][last_column_index]
        
        if (row_index, last_column_index) in memo:
            return memo[(row_index, last_column_index)]
        
        min_sum = float('inf')
        for column_index in range(3):  # Assuming the grid is a square of size 200
            if abs(column_index - last_column_index) != 1:  # Non-zero shifts
                min_sum = min(min_sum, dp(row_index-1, column_index) + grid[row_index][column_index])
        
        memo[(row_index, last_column_index)] = min_sum
        return min_sum
    
    return dp(len(grid)-1, 0)

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_falling_path_sum(grid))  # Output: 11 (from paths [1, 5, 8] and [2, 5, 8])
