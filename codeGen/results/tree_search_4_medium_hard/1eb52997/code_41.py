def count_mirrors():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N = int(input())  # Grid size
        grid = [list(input().strip()) for _ in range(N)]  # Read the grid

        # Create a 2D table to store the number of possible options
        dp = [[0] * N for _ in range(N)]

        for i in range(1, N):  # Iterate through each cell in the grid
            for j in range(1, N):
                if grid[i][j] == '.':  # If the current cell is empty
                    if grid[i-1][j] == '.':  # And the cell above it is also empty
                        dp[i][j] = dp[i-1][j] + 1  # Increment the count of possible options
                    else:
                        dp[i][j] = 0  # Reset the count if there's a rock above

        total_mirrors = sum(dp[-1])  # Sum up the counts in the last row
        print(total_mirrors)

count_mirrors()
