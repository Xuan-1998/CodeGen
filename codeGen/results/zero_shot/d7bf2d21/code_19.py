import sys

def count_LIS(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with all ones (indicating single-element subsequences)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update DP array with the maximum length of LIS ending at this position

    return max(dp)  # Return the maximum length of LIS

# Read input from stdin
arr = list(map(int, sys.stdin.readline().split()))

# Calculate and print the number of longest increasing subsequences
print(count_LIS(arr))
