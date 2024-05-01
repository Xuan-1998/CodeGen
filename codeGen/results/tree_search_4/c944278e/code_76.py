def solve():
    n = int(input())
    s = input()
    
    # Initialize memo dictionary
    memo = {}
    
    def dp(phase):
        if (phase,) in memo:
            return memo[(phase,)]
        
        winning_teams = []
        
        for i in range(2**n - 1):
            score1 = sum((s[j] == '1') << j for j in range(n))
            score2 = sum((s[j] == '0') << j for j in range(n)) - score1
            
            if (i < (1 << phase)):
                winning_teams.append(score1)
                
            elif (i >= (1 << phase) and i % (1 << phase) == 0):
                winning_teams.append(score2)
                
        memo[(phase,)] = winning_teams
        
        return winning_teams
    
    # Combine the results from each phase to get the final list of winning teams
    winning_teams = []
    
    for phase in range(n.bit_length()):
        for team in dp(phase):
            if not any(team == wteam for wteam in winning_teams):
                winning_teams.append(team)
                
    print(*winning_teams, sep='\n')
