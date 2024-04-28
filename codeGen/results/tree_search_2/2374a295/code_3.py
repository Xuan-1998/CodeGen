def solve(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = 1
            else:
                count = 0
                for p in range(1, i // (i - 1)):
                    if i % p == 0 and (i // p <= n or j < k):
                        count += dp[i // p][j - 1]
                dp[i][j] = count

    return sum(dp[n]) % 1000000007
