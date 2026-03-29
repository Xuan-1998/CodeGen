n, m, c0, d0 = map(int, input().split())
max_profit = 0
for i in range(m):
    ai, bi, ci, di = map(int, input().split())
    profit_with_stuffing = (n - ci) * di
    if ai >= bi:
        profit_without_stuffing = n * d0
    else:
        profit_without_stuffing = (n - bi) * d0
    max_profit = max(max_profit, profit_with_stuffing, profit_without_stuffing)
print(max_profit)
