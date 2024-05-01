def solve(m, N, arr):
    dp = [[0 for _ in range(N+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        dp[i][0] = 1
        for j in range(1, N+1):
            if j >= arr[i-1]:
                dp[i][j] = (dp[i-1][j] + dp[i][j-arr[i-1]]) % (10**9+7)
            else:
                dp[i][j] = dp[i-1][j]
    res = 0
    for j in range(N, -1, -1):
        if j >= arr[0]:
            res = (res + dp[m][j]) % (10**9+7)
    return res

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(m, N, arr))
