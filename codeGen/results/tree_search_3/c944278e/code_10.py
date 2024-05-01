def dp_win(matches, n):
    dp = [[0] * (1 << n) for _ in range(n)]
    for i in range(n):
        for j in range(1 << n):
            if (j >> i) & 1:
                # team i wins this match
                win = dp[i-1][j^1]
            else:
                # team i loses this match
                win = 0
            for k in range(n):
                if (k >> i) & 1 and (j >> k) & 1:
                    # both teams i and k are in the current round, so they can't both win
                    dp[i][j] += min(dp[i-1][k^1], win)
            for k in range(n):
                if (k >> i) & 1 and not (j >> k) & 1:
                    # team i wins this match, but team k is still in the current round
                    dp[i][j] += min(dp[i-1][k^1], win)
    return [team for team in range(n) if dp[n-1][1 << team]]
