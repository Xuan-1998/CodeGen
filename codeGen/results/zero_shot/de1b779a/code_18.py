# Step 1: Read the input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Initialize variables to keep track of the maximum profit
max_profit = 0

# Step 3: Iterate over each stuffing type and calculate the maximum number of buns that can be made
for ai, bi, ci, di in stuffings:
    if c0 >= ci and d0 >= bi:
        # Calculate the maximum number of buns that can be made with this stuffing
        buns = min(c0 // ci, d0 // bi)
        profit = buns * di
        max_profit = max(max_profit, profit)

# Step 4: If there is no dough left, but some stuffings are still available, try to make as many stuffed buns as possible
if c0 == 0:
    for ai, bi, ci, di in stuffings:
        if d0 >= bi and ai > 0:
            buns = min(d0 // bi, ai)
            profit = buns * di
            max_profit = max(max_profit, profit)

# Step 5: Print the maximum profit
print(max_profit)
