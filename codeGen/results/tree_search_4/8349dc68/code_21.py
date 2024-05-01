def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    def f(i, prev_max):
        if i < 0:
            return 0
        return max(arr[i-k:i+1]) + max(dp[max(0, i-k)], 0)

    for i in range(n+1):
        dp[i] = max(dp[i-1], f(i, prev_max))

    return dp[-1]

k = int(input())
arr = list(map(int, input().split()))
print(maxSumAfterPartitioning(arr, k))
