import sys

def min_replant(n, m, plants):
    # Initialize a table to store the minimum number of replanting needed
    # for each state.
    dp = [[0] * (m - 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        prev_section = plants[i - 1][1]
        min_replanted = float('inf')

        for j in range(m - 1):
            # Calculate the number of replanting needed if we move the current plant
            # to the (j + 1)-th section.
            replanted = dp[i - 1].count(0) + int(prev_section != j)

            # Update the minimum number of replanting needed.
            min_replanted = min(min_replanted, dp[i - 1][j] + replanted)

        # Update the table with the minimum number of replanting needed for this state.
        dp[i] = [x if x < min_replanted else min_replanted for x in dp[i - 1]]

    return dp[n][m - 2]


# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
plants = []
for _ in range(n):
    species, position = map(int, sys.stdin.readline().split())
    plants.append((species, position))

# Print the minimum number of replanting needed.
print(min_replant(n, m, plants))
