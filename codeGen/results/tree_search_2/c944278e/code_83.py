from math import factorial
from functools import lru_cache

@lru_cache(None)
def dp(i):
    if i == 0:
        return [[]]
    res = []
    for j in range(2**i):
        team = [j >> i-k for k in range(i)]
        winning_teams = dp(i-1)[(j >> i) % factorial[i]]
        res.append([*team, *winning_teams])
    return res

n = int(input())
result = []
for skill_levels in dp(n):
    if all(skill_levels[i] < skill_levels[i+1] for i in range(len(skill_levels)-1)):
        result.append(skill_levels)
result.sort()
print(*[' '.join(map(str, team)) for team in result], sep='\n')
