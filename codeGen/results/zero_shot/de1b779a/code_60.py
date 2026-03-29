import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
profits = [0] * (n + 1)
stuffings_left = [c0]
stuffings_required = []

for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings_left.append(stuffings_left[-1] - bi)
    stuffings_required.append(ci)

for i in range(1, n + 1):
    max_profit = 0
    for j in range(m):
        buns = min(stuffings_left[j], ci) if j else i
        profit = di * buns - (bi if j else c0) * buns
        max_profit = max(max_profit, profit)
    profits[i] = max_profit

print(profits[-1])
