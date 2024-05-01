def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [(0, 0) for _ in range(n)]

    for i in range(k):
        dp[i] = (arr[0], arr[0])

    for j in range(k, n):
        max_val = max(dp[j-k][1], arr[j])
        new_max_sum = max_val + dp[j-k][0]
        dp[j] = min((dp[j-1][0], dp[j-1][1]), (new_max_sum, max_val))

    return dp[n-1][0]

# Read input from stdin
arr = [int(x) for x in input().split()]
k = int(input())

print(max_sum_after_partitioning(arr, k))
