import sys

def maxSumAfterPartition(arr, k):
    n = len(arr)
    memo = {0: (0, float('-inf'))}

    for i in range(1, n+1):
        if i <= k:
            memo[i] = (max(memo[i-1][0], arr[i-1]), max(memo[i-1][0], arr[i-1]))
        else:
            memo[i] = (max(memo[i-k][0], arr[i-k:i]), max(memo[i-k][0], arr[i-k:i]))

    return memo[n][0]

# Read input from standard input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

print(maxSumAfterPartition(arr, k))
