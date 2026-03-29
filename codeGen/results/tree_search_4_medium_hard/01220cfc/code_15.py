===BEGIN CODE===
def can_jump(arr):
    n = len(arr)
    dp = {0: True}

    for i in range(1, n):
        dp[i] = any(j <= i - 1 and arr[j] >= i - j and dp.get(j, False) for j in range(i))

    return dp.get(n - 1, False)

===END CODE===
