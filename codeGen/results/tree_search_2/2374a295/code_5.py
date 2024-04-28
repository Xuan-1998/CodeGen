n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = 1
for j in range(2, k + 1):
    for i in range(j, n + 1):
        count = 0
        for x in range(i, 0, -1):
            if i % x == 0:
                count += dp[x][j - 1]
        print(count % 1000000007)
