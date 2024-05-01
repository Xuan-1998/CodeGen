def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        max_sum = 0
        for j in range(min(i, k), -1, -1):
            max_sum = max(max_sum, arr[i - 1])
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][min(j, i % k)] + max_sum * min(j, i // k) + (i - 1 - j) * max_sum)
    
    return dp[-1][-1]

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
