def winning_teams(n, s):
    dp = [[[] for _ in range(2**n)] for _ in range(n)]
    
    # base case: when n = 0, there are no winning teams
    if n == 0:
        return []
    
    # initialize the first state
    for i in range(2**n):
        if (i >> (n-1)) & 1:  # if the most significant bit is 1
            dp[0][i].append(1)
        else:
            dp[0][i].append(-1)
    
    # fill up the dp table using dynamic programming
    for i in range(1, n):
        for j in range(2**n):
            wins = []
            for k in range(2**n):
                if (j & k) == 0:  # if the current team loses to another team
                    if dp[i-1][k][0] > 0 and s[i-1] == 'W':
                        wins.append(dp[i-1][k][0] + 1)
                    else:
                        wins.append(-1)
                else:  # if the current team wins against another team
                    if dp[i-1][k][0] < 0 and s[i-1] == 'L':
                        wins.append(dp[i-1][k][0] - 1)
                    else:
                        wins.append(1)
            dp[i][j] = [max(wins, key=lambda x: (x, j)), list(set([i for w in wins if w > 0]))]
    
    # find all the winning teams
    winning_teams = []
    for i in range(2**n):
        if dp[n-1][i][0] > 0:
            winning_teams.extend(dp[n-1][i][1])
    return sorted(list(set(winning_teams)))
