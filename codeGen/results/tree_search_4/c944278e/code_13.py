import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, res):
    if i == 0:
        return [res]
    total = []
    for j in range(2**i-1):
        new_res = res^(s[j] & 1)
        teams = dp(i - 1, new_res)
        for team in teams:
            if not any(team & t for t in total):
                total.append(team)
    return total

n = int(input())
s = input()
result = []
for i in range(n.bit_length(), -1, -1):
    if s[i] == '1':
        result.append(2**i-1)

print(*dp(n, 0), sep='\n')
