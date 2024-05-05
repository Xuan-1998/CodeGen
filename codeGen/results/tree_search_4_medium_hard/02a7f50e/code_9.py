import sys
from bisect import bisect_left

n = int(input())
positions = []
for _ in range(n):
    a, b = map(int, input().split())
    positions.append((a, -b))  # Store beacons by their positions (in descending order) and negative power levels

positions.sort()
dp = [0] * len(positions)
prev_pos = float('inf')  # Initialize previous position as infinity
for pos, power in positions:
    idx = bisect_left(positions, pos) - 1  # Find the index of the previous beacon with a greater or equal position
    for i in range(idx, -1, -1):
        if prev_pos <= pos:  # If the current beacon is not destroyed by the previous one
            dp[i] = max(dp[i], dp[idx] + (pos - positions[i][0]))
        prev_pos = pos

print(min(dp))  # Print the minimum number of beacons that could be destroyed
