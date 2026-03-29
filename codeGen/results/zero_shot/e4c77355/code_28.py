import sys

def lis_length(arr):
    n = len(arr)
    dp = [1] * n  # initialize dp with 1s (base case)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Calculate and print the result
print(lis_length(arr))
