import sys
from math import comb
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline().strip())
    s = list(map(int, sys.stdin.readline().strip()))
    
    # Initialize the memoization dictionary
    memo = defaultdict(list)
    
    def dfs(i, mask):
        if i == 0:
            return [()]
        
        res = []
        for j in range(i):
            if ((1 << j) & mask) != 0:
                continue
            res.extend([p + [(i-1-j, s[i-1-j])]]
                          for p in dfs(j, (mask | (1 << j)))))
        return res
    
    winning_teams = []
    
    for perm in dfs(n, (1 << n) - 1):
        skill_levels = [s[perm[0]]]
        
        for i in range(1, len(perm)):
            if s[perm[i-1]] > s[perm[i]]:
                skill_levels.append(s[perm[i]])
        
        memo[tuple(skill_levels)].append(tuple(perm))
    
    for teams in memo.values():
        winning_teams.extend(sorted([team for team in teams]))
    
    print('\n'.join(map(str, winning_teams)))
