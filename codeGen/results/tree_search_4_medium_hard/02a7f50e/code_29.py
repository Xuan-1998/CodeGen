n = int(input())
b = [int(x) for x in input().split()]
max_beacon_power = max(b)

dp = [[0] * (max_beacon_power + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i
for j in range(max_beacon_power + 1):
    dp[0][j] = 0

for i in range(1, n + 1):
    for j in range(1, max_beacon_power + 1):
        if b[i-1] <= j:
            dp[i][j] = min(dp[i-1][j], f(i, j))
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
