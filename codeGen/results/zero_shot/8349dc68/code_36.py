def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        curr_max_sum = arr[i - 1]
        j = i
        while j > 0 and j <= k:
            curr_max_sum = max(curr_max_sum, arr[j - 1])
            dp[j] = max(dp[j], dp[i - j] + curr_max_sum * (j))
            j -= 1

    return dp[-1]

arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
