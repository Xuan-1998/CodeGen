import sys

n = int(input())  # Input: The initial number of beacons
beacons = []  # Store the positions and power levels of all beacons

for _ in range(n):
    a, b = map(int, input().split())  # Read the position and power level of each beacon
    beacons.append((a, b))

dp = [[0] * (100001) for _ in range(101)]

# Initialize the DP table
for j in range(100001):
    dp[0][j] = j

# Fill up the DP table
for i in range(1, 101):
    for j in range(1, 100001):
        if j <= beacons[i-1][1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][k]+1 for k in range(j+1) if k <= beacons[i-1][1])

# The minimum number of beacons that could be destroyed is stored in the last cell of the DP table
print(min(dp[-1]))
