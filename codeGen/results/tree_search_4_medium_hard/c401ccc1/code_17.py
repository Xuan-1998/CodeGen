import sys
from functools import lru_cache

@lru_cache(None)
def g(u, v):
    if u == v:
        return False
    for w in range(30):
        if (u & (1 << w)) and ((v ^ (1 << w)) & (1 << w)):
            return g(u, v ^ (1 << w))
    return True

def solve():
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        if g(u, v):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
