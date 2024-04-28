def allPossibleWinningTeams(n):
    # Initialize the table
    dp = [[0] * 2**n for _ in range(2**n)]

    # Base case: When n = 1, there's only one team that can win.
    for i in range(2**n):
        dp[i][i] = 1

    # Fill up the table using dynamic programming
    for length in range(1, n+1):
        for i in range(2**(n-length)):
            for j in range(i+1, (i|(1<<(length-1)))+1):
                if ((dp[i][j] and not dp[j][(i|j)^((1<<length)-1)]) or
                   ((not dp[i][j]) and dp[j][(i|j)^((1<<length)-1)])):
                    dp[i|(1<<(length-1))][j|(1<<(length-1))] = 1

    # Find the winning teams
    winning_teams = []
    for i in range(2**n):
        if dp[0][i]:
            winning_teams.append(bin(i)[2:].zfill(n))

    return sorted(winning_teams)
