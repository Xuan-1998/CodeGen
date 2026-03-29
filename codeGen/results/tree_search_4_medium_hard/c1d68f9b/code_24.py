import sys
from math import gcd
from functools import lru_cache

def polygon_formation(n, moods):
    @lru_cache(None)
    def dfs(i, prev_mood):
        if i > n:
            return True
        if moods[i-1] != prev_mood:
            return False
        for j in range(1, gcd(i+1, n) + 1):
            if (i+j)%n == prev_mood and dfs(i+j, 1-moods[i-1]):
                return True
        return False

    return 'YES' if dfs(n, moods[0]) else 'NO'

if __name__ == "__main__":
    n = int(input())
    moods = list(map(int, input().split()))
    print(polygon_formation(n, moods))
