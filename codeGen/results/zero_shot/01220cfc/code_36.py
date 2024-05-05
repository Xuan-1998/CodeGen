def canReachLastIndex(arr):
    n = len(arr)
    
    # Create a dp array where dp[i] is True if we can reach the ith index, and False otherwise.
    dp = [False] * (n + 1)
    dp[n - 1] = True  # We can always reach the last index.

    for i in range(n - 2, -1, -1):
        for j in range(1, arr[i] + 1):
            if i + j < n and dp[i + j]:
                dp[i] = True
                break

    return dp[0]

# Read the input array from standard input.
arr = list(map(int, input().split()))

# Print the answer to standard output.
print(canReachLastIndex(arr))
