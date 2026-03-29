from functools import lru_cache

@lru_cache(None)
def dynamic_programming(u):
    if u == 0:
        return True
    for i in range(30, -1, -1):
        if (u >> i) & 1:
            v = u ^ (1 << i)
            if dynamic_programming(v):
                return True
    return False

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if dynamic_programming(u) else "NO")
