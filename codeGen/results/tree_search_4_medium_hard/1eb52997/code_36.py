def can_place_mirror(grid):
    N = len(grid)
    memo = {}

    def helper(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # Base case: edge of grid or no rocks to East
        if i == N - 1 or j == N - 1 or grid[i][j] == '#':
            result = 0 if grid[i][j] == '.' else 1
        else:
            # Recursively call for cells above or below (i, j)
            result = 1 if all(grid[k][j] == '.' for k in range(max(0, i - 1), N)) else 0

        memo[(i, j)] = result
        return result

    total_mirrors = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and helper(i, j) == 1:
                total_mirrors += 1

    return total_mirrors

T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    print(can_place_mirror(grid))
