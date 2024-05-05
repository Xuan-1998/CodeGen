import sys
n, m, c0, d0 = map(int, sys.stdin.readline().split())
profit = 0
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    if ai >= bi and ci <= c0:
        profit += min(c0 // ci, ai // bi) * di
    c0 -= min(c0 // ci, ai // bi) * ci
print(profit)
