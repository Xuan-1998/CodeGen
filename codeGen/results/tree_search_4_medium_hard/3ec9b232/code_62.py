def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        num_multisets = 1
        for j in range(i):
            if M[j] < M[i]:
                num_multisets *= (i - j) // (j + 1)
        dp[i] = sum(dp[k] * num_multisets for k in range(j))
    return dp[n]
