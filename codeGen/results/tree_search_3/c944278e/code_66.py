def find_winning_teams(n, s):
    # Initialize the dynamic programming table
    dp = [[[] for _ in range(2**n)] for _ in range(n + 1)]
    
    # Fill up the dynamic programming table
    for i in range(n + 1):
        for j in range(2**n):
            if i == 0:
                dp[i][j] = [j]
            else:
                temp = []
                for team in dp[i - 1][j]:
                    if s[n - i][team] == 'W':
                        temp.append(team)
                dp[i][j] = temp
    
    # Find the winning teams
    result = set()
    for j in range(2**n):
        if len(dp[n][j]) > 0:
            result.add(j)
    
    # Sort and print the winning teams
    print(*sorted(list(result)), sep='\n')
