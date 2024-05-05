import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    
    # Calculate the maximum profit for this stuffing type
    max_profit = min(n // ci, ai) * (di - bi)
    
    # Update the overall maximum profit
    profit = max(profit, max_profit)

print(profit)
