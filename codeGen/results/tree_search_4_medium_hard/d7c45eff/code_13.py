import sys
from functools import lru_cache

def solve(n, k):
    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return ""  # base case for empty string
        elif j > n:
            return s[:n].repeat(k - n) + (s[n:] or "")  # duplicate the string until we reach a length of k
        else:
            min_str = min(dp(i-1, j), dp(i-1, j-1) + (s[i-1] or "")), key=lambda x: x)
            return min_str

    s = input().strip()
    print(dp(n, k))
