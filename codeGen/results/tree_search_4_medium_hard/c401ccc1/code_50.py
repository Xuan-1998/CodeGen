import sys
from functools import lru_cache

@lru_cache(None)
def and_path(u, i):
    return u & i == i

def solve():
    q = int(sys.stdin.readline())
    dp = [False] * (2**30)
    dp[0] = True

    for _ in range(q):
        u, v = map(int, sys.stdin.readline().split())
        if and_path(u, v):
            print("YES" if dp[v] else "NO")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
