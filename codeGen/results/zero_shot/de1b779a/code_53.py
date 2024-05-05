import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append((ai, bi, ci, di))

def max_buns(ai, bi, ci):
    if ai >= bi:
        return min(n // ci, ai // bi)
    else:
        return 0

def max_profit(buns):
    return sum(bi * di for bi, _ in zip(buns, stuffings))

print(max_profit([max_buns(*s) for s in stuffings]))
