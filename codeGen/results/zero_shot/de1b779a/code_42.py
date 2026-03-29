import sys

n, m, c0, d0 = map(int, input().split())
profit = 0
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    profit = max(profit, di * min(n, ai//bi) + (di - ci)//d0 * min(n, c0//ci))
print(profit)
