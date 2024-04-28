import sys
from math import comb

def find_winning_teams(n, s):
    winning_teams = set()
    
    # Iterate over all possible permutations of teams
    for i in range(comb(2**n, n)):
        team_score = 0
        for j in range(n):
            if (i >> j) & 1:
                team_score += int(s[j])
            else:
                team_score -= int(s[j])
        
        # Check if the permutation is a winning team
        if team_score > 0:
            winning_teams.add(i)
    
    return sorted(list(winning_teams))

# Test your function
n = int(input())
s = input()
print(find_winning_teams(n, s))
