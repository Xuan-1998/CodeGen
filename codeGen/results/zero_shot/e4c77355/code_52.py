import sys

def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with all ones (LIS length starting at each index)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # If current element is greater than previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update LIS length

    return max(dp)  # Return the maximum LIS length

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

print(longest_increasing_subsequence(arr))
