n = int(input())
beacons = []
for _ in range(n):
    position, power = map(int, input().split())
    beacons.append((position, power))

dp = [[float('inf')] * (1000001) for _ in range(100001)]
dp[0][j] = 0 for all j

for i in range(1, n+1):
    position, power = beacons[i-1]
    for p in range(n+1):
        if |p-position| <= power:
            dp[i][power] = min(dp[i][power], 1 + dp[p][power])
print(min(dp[n-1]))
