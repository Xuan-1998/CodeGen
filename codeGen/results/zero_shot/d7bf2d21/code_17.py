import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with all ones (length of LIS ending at each index is initially 1)

    count = 0
    max_length = 0

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        if dp[i] > max_length:
            max_length = dp[i]
            count = 1
        elif dp[i] == max_length:
            count += 1

    return count

# Read input from standard input
arr = list(map(int, input().split()))

# Call the function and print the result to standard output
print(longest_increasing_subsequences(arr))
