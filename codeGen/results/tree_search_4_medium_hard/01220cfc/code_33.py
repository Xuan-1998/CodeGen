def canJump(arr):
    dp = [False] * len(arr)
    dp[0] = True

    for i in range(len(arr)):
        if not dp[i]:
            continue
        for j in range(i-1, -1, -1):
            if j > i:
                break
            if arr[j] >= i-j+1:
                dp[i] = True
                break
    return dp[-1]
