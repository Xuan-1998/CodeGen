def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            max_sum = arr[j-1]
            for last_element_index in range(j-1, -1, -1):
                max_sum = max(max_sum, dp[i-1][last_element_index] + arr[last_element_index])
            dp[i][j] = max_sum

    return dp[n][k]

# Read the input array and k from stdin
arr = [int(x) for x in input().split()]
k = int(input())

print(maxSumAfterPartitioning(arr, k))
