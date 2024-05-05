def canJump(arr):
    n = len(arr)
    dp = [False] * n

    dp[0] = True  # base case: we can always reach the start

    for i in range(1, n):
        if not dp[i]: continue
        for j in range(i):
            if j + 1 <= i and arr[j] >= i - j:
                dp[i] = True  # if we can jump from j to i, update dp[i]
                break

    return dp[-1]

# Test the function
arr = [2,3,1,1,4]
print(canJump(arr))  # Output: True
