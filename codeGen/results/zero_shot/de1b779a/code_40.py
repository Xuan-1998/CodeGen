import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
profits = []

for i in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    total_dough_left = n - (c0 + sum(ci))
    if total_dough_left < 0:
        profits.append(0)
    else:
        max_profit = 0
        for j in range(min(total_dough_left // ci, ai) + 1):
            profit = di * min(j, ai) - bi * j - ci * j
            if profit > max_profit:
                max_profit = profit
        profits.append(max_profit)

print(max(profits))
