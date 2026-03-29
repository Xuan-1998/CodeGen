def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp with 1s, since a single element is always an increasing subsequence of length 1

    for i in range(1, n):
        for j in range(i):  # Iterate over all previous indices
            if arr[i] > arr[j]:  # If the current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update the length of the longest increasing subsequence ending at index i

    return max(dp)

# Read input from standard input
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
