def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = {i: 1 for i in range(n)}  # Initialize memoization table

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp.values())

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
