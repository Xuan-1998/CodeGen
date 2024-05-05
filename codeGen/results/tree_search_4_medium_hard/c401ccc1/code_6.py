from functools import lru_cache

@lru_cache(None)
def has_path(u):
    return u == 0 or any(has_path((u & v) >> i) for i in range(30))

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    if has_path(u):
        print("YES")
    else:
        print("NO")
