import sys

n, m, c0, d0 = map(int, input().split())
ai = [int(x) for x in input().split()]
bi = [int(x) for x in input().split()]
ci = [int(x) for x in input().split()]
di = [int(x) for x in input().split()]

max_profit = 0
current_dough = c0

for i in range(m):
    if ai[i] > 0 and current_dough >= ci[i]:
        # calculate the profit from making buns with the i-th stuffing
        profit = min(ai[i], current_dough // ci[i]) * di[i]
        max_profit += profit
        current_dough -= min(ai[i], current_dough // ci[i]) * ci[i]

print(max_profit)
