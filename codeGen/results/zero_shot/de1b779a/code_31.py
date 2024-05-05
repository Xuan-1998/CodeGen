import sys

n, m, c0, d0 = map(int, input().split())
profits = []

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    # Calculate profit for this bun type
    profit_with_stuffing = max(0, di - bi)  # subtract required stuffing cost
    profit_without_stuffing = d0 + (c0 - ci)  # use remaining dough and money
    profits.append(max(profit_with_stuffing, profit_without_stuffing))

# Calculate maximum total profit
max_profit = sum(profits)
print(max_profit)
