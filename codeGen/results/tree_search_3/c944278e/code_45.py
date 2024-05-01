def find_winning_teams(n, s):
    # Create a dictionary to store the sets of winning teams
    memo = {}
    
    def dp(i, skill_level, winning_teams):
        if i == 0:
            return {skill_level}
        
        if (i, skill_level) in memo:
            return memo[(i, skill_level)]
        
        next_winning_teams = set()
        
        for j in range(2**n):
            # Calculate the average skill level of opponents
            avg_skill_level = (skill_level + sum(s[i-1-j//2:i-1-(j+1)//2] if i >= 0 else 0)) // (2**(i-1))
            
            # Check if the team can win with its current skill level
            if s[i-1-j//2] == '1' and skill_level >= avg_skill_level:
                next_winning_teams.update(dp(i-1, skill_level+1, winning_teams | {skill_level}))
        
        memo[(i, skill_level)] = next_winning_teams
        return next_winning_teams
    
    # Initialize the base case
    winning_teams = set()
    
    for i in range(n+1):
        winning_teams.update(dp(i, 0, set()))
    
    # Sort the winning teams and print them
    return sorted(list(winning_teams))

n = int(input())
s = input()

print(find_winning_teams(n, s))
