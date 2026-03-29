def canReach(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n):
        for j in range(i - arr[i], 0, -1):
            if dp[j]:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
arr = [2,3,1,1,4]
print(canReach(arr))  # Output: True
