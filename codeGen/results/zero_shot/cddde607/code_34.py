def solve():
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0]*(k+1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = 1
                else:
                    dp[i][j][k] = 0
            elif i == 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = dp[i][j-1][arr[i][j]-1] + 1
                else:
                    dp[i][j][k] = 0
            elif j == 0:
                if arr[i][j] <= k:
                    dp[i][j][arr[i][j]] = dp[i-1][j][arr[i][j]-1] + 1
                else:
                    dp[i][j][k] = 0
            else:
                for coin in range(arr[i][j], -1, -1):
                    if arr[i][j] <= k and dp[i-1][j][coin-1] > 0:
                        dp[i][j][coin] += dp[i-1][j][coin-1]
                if arr[i][j] > k:
                    dp[i][j][k] = 0

    print(dp[-1][-1][k])
