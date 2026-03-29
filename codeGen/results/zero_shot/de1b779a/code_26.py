# Step 1: Read input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Calculate the maximum number of buns that can be made with each stuffing
buns_with_stuffing = []
for ai, bi, ci, di in stuffings:
    if ai >= bi and c0 >= ci:
        buns = min(ai // bi, c0 // ci)
        profit = (di - bi) * buns
        buns_with_stuffing.append((buns, profit))

# Step 3: Calculate the maximum number of buns that can be made without stuffing
if c0 >= d0:
    buns_without_stuffing = min(c0 // d0, n)
    profit_without_stuffing = (d0 - d0) * buns_without_stuffing

# Step 4: Calculate the maximum profit by making buns with and without stuffing
max_profit = sum([p for _, p in buns_with_stuffing])
if c0 >= d0:
    max_profit += profit_without_stuffing

print(max_profit)
