import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
available_dough = n
available_money = 0
max_profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    available_buns = min(available_dough // ci, (bi - c0) // c0)
    profit = available_buns * di
    if profit > max_profit:
        max_profit = profit

print(max_profit)
