import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: maximum sum for an empty array is 0
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], arr[i - 1])
            else:
                # Calculate the maximum sum considering the last element of the previous subarray
                # and all elements in the current subarray
                dp[i][j] = max(dp[i - 1][j], dp[i - k][j] + max(arr[i - k:i]))

    return dp[n][k]

# Read input from stdin
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(max_sum_after_partitioning(arr, k))
