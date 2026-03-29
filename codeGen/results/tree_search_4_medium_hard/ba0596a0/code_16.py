def can_cross(stones):
    n = len(stones)
    dp = [True] * (n + 1)  # dp[i] represents whether it's possible to reach stone i
    for i in range(1, n + 1):
        if not dp[i - 1]:
            continue
        for j in range(max(0, stones[i] - 2), min(n, stones[i] + 3)):
            if (j - stones[i]) % 3 == 0:
                dp[j] = True
    return dp[-1]
