def min_height_of_bookcase():
    n, m = map(int, input().split())  # Read the number of books and the maximum shelf width from stdin

    # Initialize a 2D table to store the minimum height of the bookcase for each subproblem
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill up the table using dynamic programming
    for i in range(1, n + 1):
        thickness, height = map(int, input().split())  # Read the thickness and height of the current book
        for w in range(m, -1, -1):  # Iterate through all possible shelf widths from m down to the current book's thickness
            if thickness <= w:  # If the current book fits on the current shelf
                dp[i][w] = max(height, dp[i - 1][w])  # Calculate the minimum height when i books are placed and w is the maximum shelf width
                for j in range(w):  # Iterate through all possible shelf widths from m down to the current book's thickness
                    if j + thickness <= w:  # If the combined thickness of the current book and any previous book does not exceed the shelf width
                        dp[i][w] = min(dp[i][w], max(height, dp[i - 1][j]))  # Update the minimum height by considering all possible placements

    return dp[n][m]  # Return the final answer stored in dp[n][m]

print(min_height_of_bookcase())  # Print the result to stdout
