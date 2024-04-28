def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the base case
    for i in range(k):
        dp[i][0] = arr[i]

    # Fill up the dp table
    for i in range(k, n):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], arr[i])
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + arr[i])

    # Return the maximum sum
    return max(dp[-1])

# Read input from stdin and print output to stdout
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(max_sum_after_partitioning(arr, k))
