def find_xor(A, B):
    dp = [[float('inf')] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 0

    for a in range(1, A + 1):
        for b in range(B + 1):
            if a > 0 and b >= a:
                x = min(dp[a - 1][b - a] + a, dp[0][b])
                dp[a][b] = x
            elif a <= b:
                dp[a][b] = dp[0][b]

    return -1 if dp[A][B] == float('inf') else dp[A][B]
