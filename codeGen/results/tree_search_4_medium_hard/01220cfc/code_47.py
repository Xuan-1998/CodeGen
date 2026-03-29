def can_jump(arr):
    n = len(arr)
    dp = [False] * n

    # Base case
    dp[0] = True

    for i in range(1, n):
        dp[i] = False
        for j in range(i):
            if arr[j] >= i - j and (j + 1 <= i or dp[j]):
                dp[i] = True
                break

    return dp[-1]
