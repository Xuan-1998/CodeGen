def count_words(n, m):
    MOD = 10**8 + 7
    dp = [[0]*m for _ in range(n)]

    # base case: when there are no more characters left to place in the word
    for j in range(m):
        dp[0][j] = 1

    # transition from state (n, m) to state (n-1, m-1)
    for i in range(1, n):
        if i % 2 == 0:
            for j in range(m):
                dp[i][j] = (dp[i-1][m-1] * (n - i//2)) + ((i//2 > n ? dp[i//2][m-1] * (n - i//2) : 0))
        else:
            for j in range(m):
                dp[i][j] = 0

    return dp[n-1][m-1]
