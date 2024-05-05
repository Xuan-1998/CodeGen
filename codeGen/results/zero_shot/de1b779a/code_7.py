import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append((ai, bi, ci, di))

max_profit = 0
for ai, bi, ci, di in stuffings:
    max_buns = min(n // ci, ai // bi)
    profit = max_buns * di
    if profit > max_profit:
        max_profit = profit

print(max_profit)
