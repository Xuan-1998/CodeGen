n = int(input())
beacons = []
for _ in range(n):
    a, b = map(int, input().split())
    beacons.append((a, b))

dp = [[i] * (b+1) for i, (_, b) in enumerate(beacons)]

for i in range(1, n):
    for j in range(beacons[i][1]):
        dp[i][j] = min(dp[k-1][max(0, j-beacons[k][1])] + 1 if k > 0 else i) + (1 if j > 0 else 0)
        for k in range(i):
            dp[i][j] = min(dp[i][j], dp[k][min(j, beacons[k][1])])

print(min(dp[-1]))
