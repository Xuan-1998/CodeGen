import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = arr[i-1]
            else:
                dp[i][j] = max(dp[i-1][j], arr[i-1] + dp[i-j][j-1])

    max_sum = 0
    for i in range(1, n+1):
        max_sum = max(max_sum, dp[i][n-i])
    
    return max_sum

# Read input from stdin
arr = list(map(int, input().split()))
k = int(input())

# Print the answer to stdout
print(max_sum_after_partitioning(arr, k))
