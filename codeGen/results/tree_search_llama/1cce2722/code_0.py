def max_points(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(2, n - i + 2):
            if a[i-1] == a[j+i-1]:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1]) + (i-1)
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j+1])

    return dp[-1][-1]

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
