n = int(input())
dp = [[float('inf')] * (2) for _ in range(n + 1)]
dp[0][0], dp[0][1] = 0, 50

for i in range(1, n + 1):
    t_i = int(input())
    if i % 60 == 0:
        j = 1
    else:
        j = i // 60

    for k in range(min(j, 2), -1, -1):
        dp[i][k] = min(dp[i-1][max(0, k-1)], dp[i-1][k]) + (50 if k == 1 else 120)

print(sum([dp[i][min(j, 2)] for i, j in enumerate(range(1, n+1)))]))
