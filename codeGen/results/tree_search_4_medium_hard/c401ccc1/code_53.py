import sys

q = int(input())
dp = [False] * (1 << 30)

def has_path(u, v):
    for bit in range(30):
        if ((u >> bit) & 1) and (v >> bit) & 1:
            u &= ~(1 << bit)
            return has_path(u, v)
    return True

for _ in range(q):
    u, v = map(int, input().split())
    print("YES" if has_path(u, v) else "NO")
