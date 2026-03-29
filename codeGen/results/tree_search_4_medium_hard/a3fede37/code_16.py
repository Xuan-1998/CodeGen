===BEGIN SOLUTION===
def max_path_sum(arr):
    n = len(arr)
    dp = [[float('-inf') for _ in range(n)] for _ in range(n)]

    # Base case: the maximum sum of a path from root to node i is arr[i]
    for i in range(n):
        dp[i][i] = arr[i]

    # Fill up the dynamic programming table
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            for cut in range(left, right + 1):
                dp[left][right] = max(dp[left][right], dp[left][cut] + arr[cut + 1] + dp[cut + 1][right])

    # The maximum sum of a path is stored in the top-right corner of the table
    return dp[0][n - 1]

===END SOLUTION===
