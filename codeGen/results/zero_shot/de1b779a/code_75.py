n, m, c0, d0 = map(int, input().split())
buns_no_stuffing = n // c0
buns_with_stuffing = [n // ci for _ in range(m)]
total_profit_with_stuffing = sum(max(bi, n // ci) * di for _ in range(m))
max_profit = max(buns_no_stuffing * d0, total_profit_with_stuffing)
print(max_profit)
