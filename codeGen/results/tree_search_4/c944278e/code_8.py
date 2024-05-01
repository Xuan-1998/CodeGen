import sys
from collections import namedtuple

# Define a Team named tuple to represent a team
Team = namedtuple('Team', ['skill_level'])

def solve():
    n = int(sys.stdin.readline())
    s = list(map(str, sys.stdin.read().strip().split()))
    
    # Initialize the winning_teams set
    winning_teams = set()
    
    # Use dynamic programming to find all teams that have won at least one game in each phase of the tournament
    for i in range(n):
        for j in range(2**n):
            team_skill_level = sum(int(x) for x in bin(j)[2:].zfill(n))
            dp[i][j] = any(int(x) == 1 for x in s[i]) or (all(int(x) == 0 for x in s[:i]) and dp[i-1][team_skill_level])
    
    # Iterate over all possible teams
    for j in range(2**n):
        team_skill_level = sum(int(x) for x in bin(j)[2:].zfill(n))
        if all(int(x) == 0 for x in s[:i]) or dp[i-1][team_skill_level]:
            winning_teams.add(team)
    
    # Sort the winning_teams set in ascending order and return the sorted list as the result
    print(' '.join(str(team.skill_level) for team in sorted([Team(skill_level) for skill_level in sorted(winning_teams)])))
