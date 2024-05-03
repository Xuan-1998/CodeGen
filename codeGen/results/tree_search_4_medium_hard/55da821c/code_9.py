import sys

def min_replanting(n, m, plants):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Initialize the base case
    for i in range(1, n + 1):
        if i < m:
            dp[i][1] = i

    for i in range(1, n + 1):
        prev_species = plants[i - 1][0]
        for j in range(2, min(i + 1, m) + 1):
            if j == 1 or plants[i - 1][0] != prev_species:
                dp[i][j] = min(dp[i - 1][k] + (j - 1) for k in range(j)) + 1
            else:
                dp[i][j] = min(dp[i - 1][k] for k in range(1, j))
            prev_species = plants[i - 1][0]

    return dp[n][m]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
plants = [map(int, line.split()) for line in [sys.stdin.readline() for _ in range(n)]]

print(min_replanting(n, m, plants))
