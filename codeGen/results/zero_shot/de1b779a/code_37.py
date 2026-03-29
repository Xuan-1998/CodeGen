n = int(input())
m = int(input())
c0, d0 = map(int, input().split())

stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

def max_profit(c):
    if c < 0:
        return 0
    if c == 0:
        return d0

    max_profit = 0
    for ai, bi, ci, di in stuffings:
        if c >= ci:
            profit = di - (bi + ci)
            max_profit = max(max_profit, profit + max_profit(c - ci))

    return max_profit

max_profit_total = 0
for c in range(n, 0, -1):
    max_profit_total = max(max_profit_total, max_profit(c))

print(max_profit_total)
