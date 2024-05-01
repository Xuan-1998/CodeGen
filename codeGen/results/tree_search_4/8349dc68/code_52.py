import sys

def max_sum_after_partitioning(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        for j in range(i - 1, n):
            if j < i:
                dp[i][j] = max(dp[i-1][j-1] + arr[j], arr[j])
            else:
                dp[i][j] = dp[i-1][j-k] + max(arr[j-k+1:j+1])
    
    return dp[k][n - 1]

# Read input
arr = [int(x) for x in input().split()]
k = int(input())

print(max_sum_after_partitioning(arr, k))
