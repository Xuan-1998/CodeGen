import sys
from functools import lru_cache

def solve(n, s):
    @lru_cache(None)
    def dfs(mask):
        total = 0
        for i in range(n):
            if (mask >> i) & 1:
                total += int(s[i])
        return total

    res = []
    for mask in range(1 << n):
        team_skill = dfs(mask)
        if not res or team_skill > res[0]:
            res = [team_skill]
        elif team_skill == res[0]:
            res.append(team_skill)

    print(' '.join(map(str, res)))

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
solve(n, s)
