import sys

# Read the input
n, m = map(int, input().split())
plants = []
for _ in range(n):
    _, x = map(float, input().split())
    plants.append((int(input()), x))

# Sort the plants by their positions
plants.sort(key=lambda p: p[1])

# Initialize the DP table with infinite values
dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

# Base case: no replanting needed if there are already m sections and n plants
dp[m][0] = 0

# Iterate over each plant
for i, (species, _) in enumerate(plants):
    # Find the section where this plant should be placed
    for j in range(1, min(m, species) + 1):
        # Calculate the minimum replanting if we place this plant in this section
        dp[j][i + 1] = min(dp[j][i], dp[j - 1][i - (species == j)] + (i > 0))

# Return the answer: the minimum number of plants that need to be replanted
print(min(dp[i][-1] for i in range(1, m + 1)))
