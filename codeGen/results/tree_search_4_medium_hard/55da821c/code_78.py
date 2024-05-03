def min_replanted_plants(n, m):
    # Initialize a dictionary-based memoization approach with default values of -1.
    dp = {(i, j): -1 for i in range(m) for j in range(m)}

    # Iterate through each plant, considering placing it in the section corresponding to its species.
    for _ in range(n):
        x, s = map(int, input().split())  # Read the position and species of the current plant.

        # Calculate the minimum number of plants that need to be replanted if we leave this plant where it is.
        left = dp.get((0, s), m)
        right = dp.get((m - 1, s), 0)

        # Check if moving this plant to its correct section would actually reduce the number of plants that need to be replanted.
        min_replanted = min(left, right) + 1

        # Update the state and memoization accordingly.
        for i in range(m):
            dp[(i, s)] = min(dp.get((i - 1, s), m), min_replanted)

    # Return the minimum number of plants that need to be replanted to achieve the desired arrangement.
    return dp[0][m - 1]

# Read and process the input.
n, m = map(int, input().split())
print(min_replanted_plants(n, m))
