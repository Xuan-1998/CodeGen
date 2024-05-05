import sys

n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffs = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffs.append((ai, bi, ci, di))

# Initialize maximum profit and remaining dough
max_profit = 0
remaining_dough = c0

# Iterate through each stuffing type
for i in range(m):
    # Check if there's enough dough for this stuffing
    if remaining_dough >= ci:
        # Calculate the maximum buns that can be made with this stuffing
        max_buns = min(remaining_dough // ci, ai // bi)
        # Update the maximum profit and remaining dough
        max_profit += di * max_buns
        remaining_dough -= ci * max_buns

print(max_profit)
