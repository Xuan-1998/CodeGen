import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = {}
total_dough = n
max_profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings[ai] = (bi, ci, di)

for ai, (bi, ci, di) in stuffings.items():
    if total_dough >= ci:
        profit = di - bi
        total_dough -= ci
        max_profit += profit

print(max_profit)
