def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [0] * (k + 1)

    for i in range(1, k + 1):
        if i == 1:
            dp[i] = max(arr[:i])
        else:
            for j in range(i - 2, -1, -1):
                dp[i] = max(dp[i], arr[j] + dp[i - 1])

    return dp[k]

arr = [int(x) for x in input().split()]
k = int(input())
print(max_sum_after_partitioning(arr, k))
