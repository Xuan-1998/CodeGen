def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        temp_max_sum = arr[i - 1]
        for j in range(min(i, k), -1, -1):
            temp_max_sum = max(temp_max_sum, dp[j - 1] + max(arr[i - j:i]))
        dp[i] = temp_max_sum

    return dp[-1]

arr = [int(x) for x in input().split()]
k = int(input())
print(maxSumAfterPartitioning(arr, k))
