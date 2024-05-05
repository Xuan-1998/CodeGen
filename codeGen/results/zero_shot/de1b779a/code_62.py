# Step 1: Read the input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Initialize variables to keep track of the maximum profit
max_profit = 0

# Step 3: Iterate over each stuffing and calculate the maximum profit that can be earned with that stuffing
for ai, bi, ci, di in stuffings:
    # Calculate the remaining dough after using a certain amount of stuffing
    remaining_dough = n - ci
    
    # If there's enough dough to make at least one bun with this stuffing
    if remaining_dough >= 0:
        # Calculate the maximum number of buns that can be made with this stuffing and the maximum profit that can be earned
        max_buns = min(remaining_dough // bi, ai // bi)  # Ceiling division to ensure we don't exceed available stuffing
        max_profit += max_buns * di
    else:
        # If there's not enough dough to make at least one bun with this stuffing, skip it and move on to the next one
        continue

# Step 4: Print the maximum profit that can be earned
print(max_profit)
