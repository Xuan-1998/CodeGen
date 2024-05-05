def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with 1s

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

# Print the result to stdout
print(longest_increasing_subsequence(arr))
