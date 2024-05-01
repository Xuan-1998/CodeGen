def winning_teams(n, s):
    dp = [[set(range(2**n)) for _ in range(2**n)] for _ in range(n+1)]

    for i in range(n+1):
        if i > 0:
            for j in range(2**n):
                teams = set()
                for k in range(2**n):
                    if s[i-1][k] == 'W' and j & (1 << k):
                        teams.add(k)
                dp[i][j] = teams
        else:
            dp[0][0] = set(range(2**n))

    winning_teams = set()
    for i in range(2**n):
        if not any(i & (1 << k) for k in range(n)):
            winning_teams.add(i)

    return sorted(list(winning_teams))
