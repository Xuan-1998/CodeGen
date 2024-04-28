def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_sum = 0
            for m in range(j - 1, i):
                max_sum = max(max_sum, dp[m][j - 1] + arr[m])
            dp[i][j] = max_sum

    return sum(dp[i][k] for i in range(n))

arr = [int(x) for x in input().split()]
k = int(input())

print(maxSumAfterPartitioning(arr, k))
