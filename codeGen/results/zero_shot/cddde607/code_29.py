def solve():
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j][arr[i][j]] = 1
            elif i > 0:
                if j > 0:
                    dp[i][j][min(k, arr[i][j])] += dp[i-1][j][min(k-arr[i][j], k)]
                else:
                    dp[i][j][min(k, arr[i][j])] += dp[i-1][j][min(k-arr[i][j], k)]
            elif i > 0 and j > 0:
                if k >= arr[i][j]:
                    dp[i][j][k-arr[i][j]] += dp[i-1][j][k-arr[i][j]]
                dp[i][j][min(k, arr[i][j])] += dp[i-1][j][min(k-arr[i][j], k)]

    print(dp[-1][-1][k])
