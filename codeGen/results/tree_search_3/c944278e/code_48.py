def find_winning_teams(n):
    memo = {}
    
    def dp(mask):
        if mask in memo:
            return memo[mask]
        
        winning_teams = set()
        
        for i in range(n):
            if (mask >> i) & 1:  # If the i-th phase is won by a team
                skill_level = 2 ** (n - i - 1)
                remaining_mask = mask ^ (1 << i)
                
                for j in range(2**i):
                    team_skill = skill_level | ((j >> i) & (2**(n-i-1)-1))
                    
                    # Check if the team can win given its skills in previous phases
                    if dp(remaining_mask) & (1 << n - 1 - i):
                        winning_teams.add(team_skill)
                
        memo[mask] = winning_teams
        return winning_teams
    
    mask = (1 << n) - 1
    return sorted(dp(mask))

n = int(input())
print(find_winning_teams(n))
