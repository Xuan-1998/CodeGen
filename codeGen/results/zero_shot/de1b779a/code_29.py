# Read the input values
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Sort the stuffings based on their profits
stuffings.sort(key=lambda x: (x[3] - x[2]) / x[1], reverse=True)

# Initialize variables to keep track of the maximum profit and the amount of dough left
max_profit = 0
dough_left = c0

# Iterate over the sorted stuffings
for ai, bi, ci, di in stuffings:
    # Calculate the number of buns that can be made with the current stuffing
    num_buns = min(dough_left // ci, ai // bi)
    
    # Update the maximum profit and the amount of dough left
    max_profit += num_buns * (di - ci)
    dough_left -= num_buns * ci

# If there is still some dough left, make buns without stuffing to maximize the profit
num_buns = min(dough_left // c0, n)
max_profit += num_buns * d0
dough_left -= num_buns * c0

print(max_profit)
