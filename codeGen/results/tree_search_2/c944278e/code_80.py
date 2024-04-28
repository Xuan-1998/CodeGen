import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, w):
    if i == 0:
        return []
    res = []
    for j in range(2**i):
        if (j >> (i - 1)) & 1:  # If the team wins
            if len(dp(i - 1, w | (j << (i - 1)))) > 0:
                res.append((bin(j)[2:].zfill(i), bin(w)[2:].zfill(i)))
        else:  # If the team loses
            res.extend([(bin(j)[2:].zfill(i), bin(w | (1 << i))[2:].zfill(i))] + dp(i - 1, w | (1 << i)))
    return res

n = int(input())
winning_teams = set()
for _ in range(2**n):
    w = int(input(), 2)
    if len(dp(n, w)) > 0:
        winning_teams.add(w)

print(*sorted(list(winning_teams)), sep='\n')
