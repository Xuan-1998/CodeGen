import sys

def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(n):
        max_length = 0
        for j in range(i):
            if arr[i] > arr[j]:
                max_length = max(max_length, dp[j])
        dp[i] = max_length + 1

    return max(dp)

# Read input from stdin
arr = [int(x) for x in sys.stdin.readline().split()]

# Call the function and print the result to stdout
print(longest_increasing_subsequences(arr))
