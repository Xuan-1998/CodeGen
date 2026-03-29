import sys

# Read input from stdin
n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffs = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffs.append((ai, bi, ci, di))

# Initialize maximum profit
max_profit = 0

# Iterate over each stuffing type and calculate the possible profits
for ai, bi, ci, di in stuffs:
    # Calculate the available dough and stuffing for this type
    remaining_dough = n
    remaining_stuffing = ai

    # Calculate the maximum number of buns that can be made with this type
    max_buns = min(remaining_dough // ci, remaining_stuffing // bi)

    # Calculate the profit from making these buns
    profit = max_buns * di

    # Update the maximum profit if necessary
    max_profit = max(max_profit, profit)

print(max_profit)
