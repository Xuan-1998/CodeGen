def prob(n):
    MOD = 998244353

    dp = [[False] * (n + 1) for _ in range(n + 2)]

    # Base cases: no towers or one tower is enough
    dp[0][0] = True
    for i in range(1, n + 1):
        dp[i][i] = True

    for i in range(1, n + 2):
        for j in range(i):
            if dp[j][min(j, i - j)]:
                # Check if there's a way to set signal powers
                for k in range(j + 1):
                    dp[i][k] = or_(0 <= k <= i, and_(all(not dp[m-1][min(k+1, m-k)]) for m in range(k+1)))

    # Calculate the probability
    prob = sum(1 for res in dp[n][1:])
    return pow(prob, MOD - 2, MOD)
