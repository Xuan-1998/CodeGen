def partitionArray(n):
    arr = list(map(int, input().split()))
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if prefix_sum[j] == prefix_sum[i]:
                dp[i][j] = dp[i+1][j-1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(partitionArray(n))
