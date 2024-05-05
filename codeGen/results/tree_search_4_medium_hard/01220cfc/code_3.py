def can_reach_last_index(arr):
    n = len(arr)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n + 1):
        if arr[i - 1] >= i - 1 and dp[i - 1]:
            dp[i] = True
        else:
            dp[i] = False

    return dp[n]
