import sys

# Step 1: Read the input
n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Calculate the maximum number of buns that can be made with each stuffing
buns = []
for ai, bi, ci, di in stuffings:
    buns.append(min(n, n // (ci + bi)))

# Step 3: Find the maximum profit by making different numbers of buns with each stuffing
max_profit = 0
for i in range(len(buns)):
    for j in range(i+1):
        max_profit = max(max_profit, d0 + di * min(n, sum(min(x, y) for x, y in zip(stuffings[i][2:], stuffings[j:]))))

print(max_profit)
