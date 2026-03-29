import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
profit = 0
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    with_stuffing_profit = min(n // ci, ai // bi) * (di - c0)
    without_stuffing_profit = (n - d0) * (d0 / 2)
    profit += max(with_stuffing_profit, without_stuffing_profit)

print(profit)
