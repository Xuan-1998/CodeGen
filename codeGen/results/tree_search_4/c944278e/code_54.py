def winning_teams(n, s):
    dp = [[set() for _ in range(n + 1)] for _ in range(n + 1)]
    
    # Base case: Initialize dp[0][j] for all j
    for j in range(n + 1):
        if s[j - 1] == '1':
            dp[0][j].add(2 ** (n - j))
    
    # Iterate through each phase i from 0 to n-1
    for i in range(n):
        for j in range(i, n + 1):
            # Update state by considering all combinations of winning and losing outcomes
            for team in dp[i][j]:
                if s[i] == '1':
                    dp[i + 1][j].add(team * 2)
                else:
                    dp[i + 1][j].add(team | (2 ** (n - j)))
    
    # Return the set of teams that have won at least one game
    return dp[n][n]
