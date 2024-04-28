import sys

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = arr[i-1]
            else:
                dp[i][j] = max(dp[i-1][min(j, k)] + arr[i-1], dp[i-1][j-k+1] + arr[i-1])

    return dp[-1][-1]

# Input
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Process the input
max_sum = maxSumAfterPartitioning(arr, k)

# Print the output
print(max_sum)
