from math import comb
from functools import lru_cache

def solve(n, s):
    @lru_cache(None)
    def is_win(team):
        return sum(int(b) for b in s) - team >= 0

    winning_teams = set()
    for i in range(1 << n):  # iterate over all possible combinations of teams
        team = sum((i >> j) & 1 for j in range(n))  # get the skill level of the current team
        if is_win(team):
            winning_teams.add(team)

    return sorted(winning_teams)

n = int(input())
s = input().strip()
print(*solve(n, s), sep='\n')
