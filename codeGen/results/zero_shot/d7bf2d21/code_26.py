import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with 1s

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Calculate the number of longest increasing subsequences
max_lis_length = lis_length(arr)

print(max_lis_length)
