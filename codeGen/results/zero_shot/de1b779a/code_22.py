import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffs = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin readline().split())
    stuffs.append((ai, bi, ci, di))

def calculate_profit(stuffs):
    max_buns = 0
    for ai, bi, ci, di in stuffs:
        remaining_dough = n - ci
        if remaining_dough >= 0 and ai >= bi:
            buns = min(remaining_dough // ci, ai // bi)
            max_buns += buns
            remaining_dough -= buns * ci
    return d0 * n + sum(di * buns for ai, bi, ci, di in stuffs for buns in range(min(remaining_dough // ci, ai // bi) + 1))

print(calculate_profit(stuffs))
