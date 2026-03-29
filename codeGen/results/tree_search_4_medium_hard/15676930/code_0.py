def max_joys():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, 2)+1):
            if i == 1:
                dp[i][j] = a[0]
            elif j == 0:
                dp[i][j] = max(dp[i-1][0], dp[i-2][1] + b[0])
            else:
                dp[i][j] = max(dp[i-1][0], dp[i-2][1] + c[0])

    return dp[n][n]
