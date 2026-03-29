# Step 1: Read input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Sort the stuffings by profit per unit of dough
stuffings.sort(key=lambda x: (x[3] - x[1]) / x[2], reverse=True)

# Step 3: Initialize variables for maximum profit and remaining dough
max_profit = 0
remaining_dough = c0

# Step 4: Iterate through the stuffings to find the maximum profit
for ai, bi, ci, di in stuffings:
    if remaining_dough >= ci:
        # Calculate the number of buns that can be made with this stuffing
        buns = min(remaining_dough // ci, n)
        max_profit += (di - bi) * buns
        remaining_dough -= bi * buns
    else:
        break

# Step 5: Print the maximum profit
print(max_profit)
