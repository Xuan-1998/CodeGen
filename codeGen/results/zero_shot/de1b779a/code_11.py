import sys

# Read input from stdin
n, m, c0, d0 = map(int, sys.stdin.readline().split())
a = []
b = []
c = []
d = []

for i in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

# Calculate the maximum profit for each case
max_profit_without_stuffing = max(0, n - c0) * d0

max_profit_with_stuffing = 0
for i in range(m):
    if a[i] > 0 and b[i] <= n:
        remaining_dough = n - c[i]
        profit_per_bun = min(a[i], remaining_dough) * (d[i] - c[i])
        max_profit_with_stuffing += profit_per_bun
        n -= c[i]

# Choose the case that yields the highest profit
max_profit = max(max_profit_without_stuffing, max_profit_with_stuffing)

# Print the answer to stdout
print(max_profit)
