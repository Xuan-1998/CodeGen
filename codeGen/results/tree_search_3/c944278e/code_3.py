import sys

def find_winning_teams(n, s):
    # Convert binary string to integer representation
    total_permutations = 2 ** n
    
    winning_teams = []
    
    for i in range(total_permutations):
        team_skill_levels = [0] * n
        
        for j in range(n):
            if (i >> j) & 1:
                team_skill_levels[j] = 1
        
        # Check if this permutation of team skill levels can lead to a winning scenario
        is_winning_team = True
        
        for k in range(2 ** n):
            current_winner = sum((k >> i) & 1 for i in range(n))
            
            # If the current winner does not match the expected winner, it's not a winning team
            if s[k] != str(current_winner):
                is_winning_team = False
                break
        
        if is_winning_team:
            winning_teams.append(team_skill_levels)
    
    return winning_teams

if __name__ == "__main__":
    n = int(input())
    s = input()
    
    winning_teams = find_winning_teams(n, s)
    
    for team in winning_teams:
        print(" ".join(map(str, team)))
