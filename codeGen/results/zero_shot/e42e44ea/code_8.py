def min_points_recursive(grid, i, j, points):
    # Base case: reached the bottom-right cell
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        return points
    
    # Check if we can move down or right
    down_possible = i < len(grid) - 1 and grid[i + 1][j] > 0
    right_possible = j < len(grid[0]) - 1 and grid[i][j + 1] > 0
    
    # Try moving down if possible
    if down_possible:
        points_down = min_points_recursive(grid, i + 1, j, points)
        if points_down != -1:
            return points_down
    
    # Try moving right if possible
    if right_possible:
        points_right = min_points_recursive(grid, i, j + 1, points)
        if points_right != -1:
            return points_right
    
    # If we can't move down or right, return -1
    return -1

# Call the recursive function with the initial points and position
def find_min_points(N, M, grid):
    min_points = float('inf')
    for i in range(M):
        for j in range(N):
            if grid[i][j] > 0:
                points = min_points_recursive(grid, 0, 0, 0)
                if points != -1 and points < min_points:
                    min_points = points
    return min_points

# Read input from stdin
N, M = map(int, input().split())
grid = []
for _ in range(M):
    row = list(map(int, input().split()))
    grid.append(row)

# Call the find_min_points function and print the result to stdout
print(find_min_points(N, M, grid))
