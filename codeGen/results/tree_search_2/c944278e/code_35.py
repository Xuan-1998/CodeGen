import sys
from math import comb
from itertools import permutations

def solve():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    # Calculate the total number of teams
    total_teams = 2**n
    
    # Initialize a set to store all winning teams
    winning_teams = set()
    
    for perm in permutations(s):
        current_score = 0
        for i, team in enumerate(perm):
            if team == '1':
                current_score += comb(n-i-1, n)
        
        # If the current score is greater than or equal to total_teams/2,
        # then this permutation represents a winning team
        if current_score >= total_teams//2:
            winning_teams.add(int(''.join(perm), 2))
    
    # Sort and print all winning teams in ascending order
    for team in sorted(winning_teams):
        print(team)

if __name__ == "__main__":
    solve()
