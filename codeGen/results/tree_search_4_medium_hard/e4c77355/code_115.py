def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [-float('inf')] * (n + 1)

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[n - 1]

# Read input from stdin
arr = [int(x) for x in input().split()]

print(longest_increasing_subsequence(arr))
