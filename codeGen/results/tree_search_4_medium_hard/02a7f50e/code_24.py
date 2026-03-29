import sys

n = int(sys.stdin.readline())
beacons = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    beacons.append((a, b))

dp = [[0] * 100001 for _ in range(100000)]
dp[0][0] = n

for i, (a, b) in enumerate(beacons):
    p = sum(1 for k in range(i+1) if beacons[k][0] <= a and beacons[k][1] >= b)
    for j in range(min(b, 100000), -1, -1):
        dp[a][j] = min(dp[a-1][p-1], p + 1)

print(min(dp[-1]))
