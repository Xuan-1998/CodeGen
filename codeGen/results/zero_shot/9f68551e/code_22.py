import sys

def min_mana(n, k, h):
    k.sort()
    mana = 0
    for i in range(n):
        while k[i] > 0 and h[i] >= k[i]:
            mana += k[i]
            k[i] -= 1
            if k[i] == 0:
                break
    return mana

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    k = list(map(int, sys.stdin.readline().split()))
    h = list(map(int, sys.stdin.readline().split()))
    print(min_mana(n, k, h))
