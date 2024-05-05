import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with all ones

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum length of LIS

# Read input from stdin
arr = [int(x) for x in input().split()]

print(lis_length(arr))
