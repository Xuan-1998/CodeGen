import sys

def infinite_zoo(u, v):
    xor = u ^ v
    if xor == 0:
        return "NO"
    subset = True
    for i in range(30):  # iterate up to 2^30-1
        bit_set_in_v = (v & (1 << i)) != 0
        if not bit_set_in_v or (u & (1 << i)) == 0:
            subset = False
            break
    return "YES" if subset else "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(infinite_zoo(u, v))
