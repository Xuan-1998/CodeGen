n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

dp = [[float('inf')] * (max(b) + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(max(beacons[i-1][1]), -1, -1):
        if j >= beacons[i-1][1]:
            dp[i][j] = min(dp[i-1][max(0, j-beacons[i-1][1])] + 1, dp[i-1][k] + 1) for k in range(min(j, beacons[i-2][1]))
        else:
            dp[i][j] = dp[i-1][j]

print(min(dp[-1]))
