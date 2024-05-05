import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def count_teams(total_players, n):
    if total_players < n:
        return 0
    elif total_players == n:
        return 1
    else:
        return 1 + count_teams(total_players - n, n)

m = int(input())
s = list(map(int, input().split()))
h = int(input()) - 1

total_players = sum(s)
if total_players < n:
    print(-1)
else:
    num_teams = count_teams(total_players, n)
    p = (sum(1 if i == h else s[i] // (n - 1) for i in range(m)) + 1) / num_teams
    print(p)
