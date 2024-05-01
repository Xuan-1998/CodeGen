import sys
from functools import lru_cache

def solve():
    n = int(input())
    s = input()
    
    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return 0
        if s[i-1] == '1':
            return max(dp(i-1, j), j+1)
        else:
            return dp(i-1, j)

    winning_teams = set()
    for j in range(2**n):
        if dp(n, j) > 0:
            winning_teams.add(j)

    print(*sorted(winning_teams))

if __name__ == "__main__":
    solve()
