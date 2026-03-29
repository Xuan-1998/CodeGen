import sys

# Read input from stdin
n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append((ai, bi, ci, di))

# Initialize maximum profit and available dough
max_profit = 0
available_dough = n

# Iterate through each stuffing type
for stuffing in stuffings:
    ai, bi, ci, di = stuffing
    
    # Calculate the maximum number of buns that can be made with this stuffing
    max_buns = min(available_dough // ci, (n - c0) // ci)
    
    # Update available dough and calculate profit for this stuffing
    available_dough -= max_buns * ci
    max_profit += di * max_buns

# Print the maximum profit
print(max_profit)
