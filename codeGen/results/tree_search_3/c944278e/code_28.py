def winning_teams(n, s):
    # Initialize the dp array to store the maximum skill level reached at each step
    dp = [0] * (1 << n)
    
    # Initialize the list of winning teams
    winning_teams = []
    
    for mask in range(1 << n):
        # Calculate the total skill level of the current team
        team_skill = sum(s[i] for i in range(n) if (mask & (1 << i)) > 0)
        
        # If this is not a winning team, we can skip it
        if len(winning_teams) == 0 or team_skill < dp[~mask]:
            continue
        
        # Add the current team to the list of winning teams
        winning_teams.append(team_skill)
    
    return sorted(winning_teams)

n = int(input())
s = [int(x) for x in input().split()]
print(*winning_teams(n, s), sep='\n')
