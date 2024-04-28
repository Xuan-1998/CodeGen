def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            if j == 1:
                dp[i][j] = max(arr[i-1], dp[i-1][j])
            else:
                dp[i][j] = max(dp[i-1][j-1] + arr[i-1], dp[i-1][j])

    return dp[-1][-1]

k = int(input())
arr = list(map(int, input().split()))
print(maxSumAfterPartitioning(arr, k))
