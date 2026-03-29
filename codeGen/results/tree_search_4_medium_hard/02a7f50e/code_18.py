import sys

def min_beacons_destroyed(n, positions, powers):
    # Initialize the DP table with dimensions n x (max(b_i) + 1)
    dp = [[i for _ in range(max(powers) + 1)] for i in range(n)]

    # Initialize the first row of the DP table
    for j in range(max(powers) + 1):
        if powers[0] <= j:
            dp[0][j] = 0
        else:
            dp[0][j] = positions[0]

    # Fill up the DP table using the recurrence relation
    for i in range(1, n):
        for j in range(max(powers) + 1):
            if powers[i] <= j:
                dp[i][j] = min(dp[k][min(j, powers[k])] + 1 for k in range(i))
            else:
                dp[i][j] = i

    # Return the minimum number of beacons that could be destroyed
    return min(dp[-1])

# Read input from stdin
n = int(input())
positions = []
powers = []
for _ in range(n):
    a, b = map(int, input().split())
    positions.append(a)
    powers.append(b)

print(min_beacons_destroyed(n, positions, powers))
