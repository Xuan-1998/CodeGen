def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dynamic programming array with ones

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum length of the longest increasing subsequence


# Read input from standard input
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
