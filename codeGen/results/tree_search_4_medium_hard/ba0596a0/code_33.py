def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * n

    dp[0] = True  # Frog starts on the first stone

    for i in range(1, n-1):
        for j in range(max(0, i-k), min(n, i+k+1)):
            if abs(i-j) in (k-1, k, k+1) and dp[j]:
                dp[i] = True
                break

    return dp[n-1]
