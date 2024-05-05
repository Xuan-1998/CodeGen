m, n = [int(x) for x in input().split()]
grid = [[int(x) for x in input().split()] for _ in range(m)]

def min_sum(i, j):
    if i == m-1 and j == n-1:  # base case: we're at the bottom-right corner
        return grid[i][j]
    elif i < m-1:  # move down
        return grid[i][j] + min_sum(i+1, j)
    elif j < n-1:  # move right
        return grid[i][j] + min_sum(i, j+1)
    else:
        raise ValueError("Invalid position")

print(min_sum(0, 0))
