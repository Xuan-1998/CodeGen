def canJump(arr):
    n = len(arr)
    dp = [False] * n

    for i in range(n):
        if i == 0:
            dp[i] = True
        elif dp[i-1]:
            j = max(0, i-arr[i])
            if j >= n - 1 or dp[j]:
                dp[i] = True

    return dp[-1]
