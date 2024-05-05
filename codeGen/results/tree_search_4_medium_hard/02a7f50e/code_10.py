from collections import defaultdict

dp = defaultdict(int)

def calculate_min_destroyed(beacons):
    n = len(beacons)
    beacons.sort(key=lambda x: x[0])  # Sort beacons by position

    for i in range(n):
        dp[i] = [float('inf')] * (beacons[i][1] + 1)  # Initialize DP table
        dp[i][0] = 0  # No destruction needed when power is 0

        for j in range(beacons[i][1], -1, -1):
            dp[i][j] = min(dp[i-1][max(0, j-1)] + (beacons[i][0]-beacons[i-1][0]) if i > 0 else 0,
                           dp[i][j-1])

    return dp[n-1][-1]

n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

print(calculate_min_destroyed(beacons))
