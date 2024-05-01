def find_winning_teams():
    n = int(input())
    s = input()
    
    # Initialize dp array with zeros, where dp[i][j] represents the number of ways the j-th team can win up to i phases
    dp = [[0] * (2 ** n) for _ in range(n + 1)]
    
    # Iterate through each phase and update the dp array based on whether the current bit is '1' or '0'
    for i in range(1, n + 1):
        for j in range(2 ** n):
            if (s[i - 1] == '1'):
                dp[i][j] = sum(dp[i - 1][k] for k in range(2 ** n) if ((j >> (n - i)) & 1) ^ ((k >> (n - i)) & 1))
            else:
                dp[i][j] = sum(dp[i - 1][k] for k in range(2 ** n) if (j & (1 << (n - i))) == 0 or ((k >> (n - i)) & 1) ^ (s[i - 1] == '1'))
    
    # Find the winning teams by iterating through the dp array and checking which team has won at least one game in each phase
    winning_teams = set()
    for j in range(2 ** n):
        if any(dp[n][j]):
            winning_teams.add(j)
    
    # Print the winning teams in ascending order
    print(*sorted(list(winning_teams)), sep='\n')

find_winning_teams()
