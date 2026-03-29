import sys

def min_destroyed_beacons(n, positions, powers):
    dp = [[0] * (max(powers) + 1) for _ in range(n)]

    # Initialize the DP table
    for i in range(1, n):
        for j in range(max(powers) + 1):
            if j < powers[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][k] + 1 for k in range(j, max(powers) + 1))

    # Find the minimum number of beacons that could be destroyed
    return min(dp[-1])

# Receive input from stdin
n = int(input())
positions = []
powers = []
for _ in range(n):
    a, b = map(int, input().split())
    positions.append(a)
    powers.append(b)

print(min_destroyed_beacons(n, positions, powers))
