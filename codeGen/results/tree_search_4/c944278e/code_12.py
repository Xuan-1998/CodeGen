def findWinningTeams(n):
    # Initialize dp with zeros
    dp = [[0] * (2**n) for _ in range(n+1)]

    # Base case: when n == 1, there is only one winning team
    dp[0][0] = 2**n

    # Dynamic programming approach
    for i in range(1, n+1):
        for j in range(2**i):
            if j < 2**(i-1):
                # Team wins all matches in the current phase
                dp[i][j] = dp[i-1][0]
            else:
                # Team loses all but one match in the current phase
                dp[i][j] = dp[i-1][2**(i-1)-1]

    return [i for i in range(2**n) if dp[n][i] > 0]
