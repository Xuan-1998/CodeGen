def count_paths(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    dp[0][0][0] = 1
    for i in range(1, n):
        dp[i][0][0] = dp[i-1][0][0]
        for j in range(1, n):
            if arr[i][j] <= k:
                dp[i][j][0] += dp[i-1][j][0] + dp[i][j-1][0]
            else:
                break
    res = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= k and (i == n - 1 or j == n - 1):
                res += dp[i][j][arr[i][j]]
    return res

k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(count_paths(k, n, arr))
