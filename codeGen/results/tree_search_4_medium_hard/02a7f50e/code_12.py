n = int(input())
beacons = [0] + [int(x) for x in input().split()]
dp = [[float('inf')] * (1000001) for _ in range(n+1)]

for i in range(n):
    for j in range(1000001):
        if not beacons[i]:
            dp[i+1][j] = 0
        else:
            dp[i+1][j] = min(dp[i][max(0,j-b_i)] + 1, sum((dp[k][max(0,j-b_k)] or i-k) for k in range(i)))

print(dp[-1][-1])
