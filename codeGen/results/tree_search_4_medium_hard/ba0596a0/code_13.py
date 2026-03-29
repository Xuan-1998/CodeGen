def can_cross(stones):
    n = len(stones)
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if abs(i-j) in {stones[i]-stones[j], stones[i]-stones[j]+1, stones[i]-stones[j]-1}:
                dp[i] = max(dp[i], dp[j])
            elif (stones[i]-stones[j]) % 3 == ((stones[i]-stones[0]) // 3) % 3:
                dp[i] = max(dp[i], dp[j])

    return dp[-1] > 0
