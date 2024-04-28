import sys
from functools import lru_cache

def win_teams(n, s):
    @lru_cache(None)
    def dp(i, mask):
        if i == 0:
            return [[]]
        
        res = []
        for j in range(i):
            if (mask >> j) & 1:
                for team in dp(j, mask ^ (1 << j)):
                    res.append([s[i-1]] + team)
            else:
                for team in dp(j, mask | (1 << i)):
                    res.append([s[i-1]] + team)
        
        return res
    
    @lru_cache(None)
    def find_win_teams(i):
        if i == 0:
            return [[]]
        
        res = []
        for j in range(i):
            if (mask >> j) & 1:
                for team in find_win_teams(j):
                    res.append([s[i-1]] + team)
            else:
                for team in find_win_teams(j):
                    res.append([s[i-1]] + team)
        
        return res
    
    mask = int('1' * n, 2)
    teams = dp(n, mask)
    
    win_teams = set()
    for team in teams:
        if all(s[j] > '0' for j in range(len(team))):
            win_teams.add(tuple(sorted(team)))
    
    print('\n'.join(map(str, sorted(list(win_teams)))))
