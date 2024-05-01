import sys
from functools import lru_cache

def solve(n, s):
    @lru_cache(None)
    def dp(i, j):
        if i == n:
            return [1 << j]
        res = []
        if (s[i] >> (n - 1 - i)) & 1:
            for k in range(2 ** (i + 1)):
                if ((k >> (i + 1 - i)) & 1) == s[i]:
                    res.extend(dp(i + 1, k))
        return res

    winning_teams = dp(0, 0)
    winning_teams.sort()
    return "\n".join(map(str, winning_teams))

if __name__ == "__main__":
    n = int(input())
    s = input().rstrip()
    print(solve(n, s))
