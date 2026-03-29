def canJump(arr):
    n = len(arr)
    dp = [False] * n

    dp[0] = True

    for i in range(1, n):
        if not dp[i]:
            for j in range(i):
                if j + arr[j] >= i and dp[j]:
                    dp[i] = True
                    break

    return dp[-1]
