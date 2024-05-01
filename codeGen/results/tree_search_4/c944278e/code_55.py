import sys
from collections import deque

def solve(n, s):
    memo = {}
    win_teams = set()

    def state_transition(i):
        if i in memo:
            return memo[i]

        teams = set()
        for team in range(2**n):
            if (team >> (i-1)) & 1:  # Check if the team wins in phase i
                teams.add(team)
            else:
                teams.difference_update({team})

        memo[i] = teams
        return teams

    for i in range(n, -1, -1):
        teams = state_transition(i+1)
        if len(teams) > 0 and (len(teams) == 2**i or i == n-1):
            win_teams.update(teams)

    return sorted(list(win_teams))

n = int(sys.stdin.readline())
s = sys.stdin.read().strip()
print(solve(n, s))
