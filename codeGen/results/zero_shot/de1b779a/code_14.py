import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
d0 = int(sys.stdin.readline())
c0 = int(sys.stdin.readline())
d0 = int(sys.stdin.readline())

max_profit = 0

for i in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    
    # Calculate the maximum profit for this stuffing type
    max_buns = min(n // ci, ai // bi)  # Calculate the number of buns that can be made without running out of dough or stuffing
    profit = (di - c0) * max_buns
    
    # Update the overall maximum profit
    max_profit = max(max_profit, profit)

print(max_profit)
