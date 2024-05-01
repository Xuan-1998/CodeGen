from functools import lru_cache

def solve(n, s):
    @lru_cache(None)
    def dp(mask):
        if mask == 0: return 1
        res = 0
        for i in range(n-1, -1, -1):
            if (mask >> i) & 1:
                res += dp(mask ^ (1 << i))
        return res

    winning_teams = []
    for i in range(2**n):
        if s[i] == 'W': continue
        mask = (1 << n) - 1
        for j in range(n-1, -1, -1):
            if ((i >> j) & 1) != (s[j] == 'L'):
                mask ^= 1 << j
        if dp(mask):
            winning_teams.append(i)
    return sorted(winning_teams)

n = int(input())
s = input()
print(*solve(n, s), sep='\n')
