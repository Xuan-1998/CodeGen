def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [0] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Read input array from stdin
arr = list(map(int, input().split()))

# Calculate and print the length of the longest increasing subsequence
print(longest_increasing_subsequence(arr))
