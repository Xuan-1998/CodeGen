import sys
from functools import lru_cache

def solve(n, s):
    @lru_cache(None)
    def dfs(i):
        if i == n:
            return [1]
        res = []
        for j in range(2**i):
            if (j & ((1 << i) - 1)) == (s[:i] >> (n - i - 1)).index(1):
                teams = dfs(i + 1)
                res.extend([team | (1 << i) for team in teams])
        return res

    winning_teams = set()
    for team in dfs(0):
        if any(((team >> i) & 1) == ((other_team >> i) & 1) and i < n for other_team in winning_teams)):
            continue
        winning_teams.add(team)
    return sorted(list(winning_teams))

n = int(input())
s = input()
print(*solve(n, s), sep='\n')
