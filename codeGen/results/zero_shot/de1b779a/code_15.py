# Read input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Sort the stuffings by their profit per unit of dough
stuffings.sort(key=lambda x: (x[3] - x[2]) / x[1], reverse=True)

# Initialize variables for maximum profit and remaining dough
max_profit = 0
remaining_dough = c0

# Iterate over the sorted stuffings
for ai, bi, ci, di in stuffings:
    # Calculate how many buns can be made with the current stuffing
    buns = min(remaining_dough // ci, (d0 - remaining_dough) // bi)
    
    # Update maximum profit and remaining dough
    max_profit += buns * di
    remaining_dough -= buns * ci

print(max_profit)
