def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        currMax = arr[i - 1]
        for j in range(min(i, k), -1, -1):
            currMax = max(currMax, arr[i - j - 1])
            dp[i] = max(dp[i], dp[i - j] + currMax * j)
    return dp[-1]

arr = [int(x) for x in input().split()]
k = int(input())
print(maxSumAfterPartitioning(arr, k))
