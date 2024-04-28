import itertools
from collections import Counter

def is_winning_team(team):
    n = len(team)
    skill_levels = [team[i] ^ (n - i - 1) for i in range(n)]
    return sum(skill_levels) > 0

def solve():
    n = int(input())
    teams = [input() for _ in range(2**n)]
    
    winning_teams = []
    for team_permutation in itertools.permutations(teams):
        if is_winning_team(team_permutation):
            winning_teams.append(''.join(team_permutation))
    print(*sorted(set(winning_teams)), sep='\n')

solve()
