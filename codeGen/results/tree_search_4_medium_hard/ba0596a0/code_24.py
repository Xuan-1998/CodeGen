def can_cross_stones(stones):
    n = len(stones)
    dp = [[False] * 3 for _ in range(n)]
    memo = [False, False, True]

    dp[0][0] = True

    for i in range(1, n):
        for k in range(3):
            j = i - 1
            while j >= 0 and not memo[k-1]:
                j -= 1
            if j >= 0:
                dp[i][k] = any(dp[j][l] for l in (min(k-1, k, k+1),))
            else:
                break

    return any(dp[n-1])

