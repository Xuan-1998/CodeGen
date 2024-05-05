import sys

def min_operations(arr):
    n = len(arr)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        max_j = -1
        for j in range(i):
            if arr[j] < arr[i]:
                max_j = j
        if max_j != -1:
            dp[i] = min(dp[max_j] + 1, dp[i])
        else:
            dp[i] = 0

    return dp[-1]

# Read input from stdin
n = int(input())
arr = list(map(int, input().split()))

print(min_operations(arr))
