import sys

n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

dp = [[0] * (b + 1) for _ in range(n)]

# Initialize the base case: no destruction occurs when there are no activated beacons
for j in range(1, 1000001):
    dp[0][j] = 0

for i in range(n):
    for j in range(1, 1000001):
        min_destructions = sys.maxsize
        for k in range(i):
            if j <= beacons[k][1]:
                # Calculate the destructions caused by the newly added beacon at position i with power level j
                destructions = dp[k][max(0, j - beacons[k][1])] + (i - k)
                min_destructions = min(min_destructions, destructions)
        dp[i][j] = min_destructions

# Find the minimum number of destructions that could occur when exactly one beacon is added
min_destructions = sys.maxsize
for j in range(1, 1000001):
    if j <= beacons[-1][1]:
        min_destructions = min(min_destructions, dp[-1][max(0, j - beacons[-1][1])])

print(min_destructions)
