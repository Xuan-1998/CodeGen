import sys
from functools import lru_cache

@lru_cache(None)
def dp(x, n):
    if x == 0:
        return -1
    if n < 0:
        return float('inf')
    if n == 0:
        return 0

    d = (x % 10)
    if d != 0:
        res = dp(int(x / 10), n-1) + 1
    else:
        res = dp(1, n-1) + 1

    return min(res, dp(x, n-1))

def main():
    n, x = map(int, input().split())
    print(dp(x, n))

if __name__ == "__main__":
    main()
