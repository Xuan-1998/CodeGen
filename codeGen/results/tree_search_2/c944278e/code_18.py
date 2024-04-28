import sys
from math import comb

def solve(n, s):
    winning_teams = []
    for team in range(2**n):
        # Convert the binary representation to decimal and create a list of skills
        skill_levels = [int(x) for x in bin(team)[2:].zfill(n)]
        
        # Check if this permutation is a winning team
        is_winning_team = True
        for i in range(n-1):
            if s[i] == '0' and skill_levels[i] > 0:
                is_winning_team = False
                break
        
        # If this permutation is a winning team, add it to the list of winning teams
        if is_winning_team:
            winning_teams.append(team)
    
    return [team for _, team in sorted((comb(n-1, i), team) for i, team in enumerate(winning_teams))]

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
print(*solve(n, s), sep='\n')
