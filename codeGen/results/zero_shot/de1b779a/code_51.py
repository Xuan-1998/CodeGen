import sys

# Read input values from stdin
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
c0, d0 = map(int, sys.stdin.readline().split())

max_profit = 0
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())

    # Calculate the maximum number of buns that can be made with this stuffing type
    max_buns_with_stufing = min(n // ci, ai // bi)
    profit_with_stufing = max_buns_with_stufing * (di - bi)

    # Calculate the maximum number of buns that can be made without any stuffing
    max_buns_without_stufing = n // c0

    # Calculate the profit for this stuffing type and without any stuffing
    profit_without_stufing = max_buns_without_stufing * d0

    # Update the maximum profit
    max_profit = max(max_profit, profit_with_stufing, profit_without_stufing)

# Print the maximum profit to stdout
print(max_profit)
