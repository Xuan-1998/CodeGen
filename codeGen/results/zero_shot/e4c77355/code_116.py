def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # Initialize dp array with all ones (LIS length for each element is 1 initially)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:  # Check if current element is greater than the previous one
                dp[i] = max(dp[i], dp[j] + 1)  # Update LIS length if a longer subsequence is found

    return max(dp)

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
