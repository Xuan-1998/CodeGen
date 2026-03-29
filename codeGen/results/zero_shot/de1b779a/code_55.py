# Step 1: Read input from standard input
n, m, c0, d0 = map(int, input().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    stuffings.append((ai, bi, ci, di))

# Step 2: Sort the stuffing types by their profits
stuffings.sort(key=lambda x: (x[3] - (x[1] * c0) / x[2]) if x[1] > 0 else (d0 + x[3]), reverse=True)

# Step 3: Initialize variables to keep track of the maximum profit and the number of buns made
max_profit = 0
buns_made = 0

# Step 4: Iterate over the stuffing types and calculate the maximum number of buns that can be made with each type
for ai, bi, ci, di in stuffings:
    while n >= ci and bi > 0:
        if (bi * c0) / ci + di > d0:
            buns_made += 1
            max_profit += di
            n -= ci
            bi -= 1
        else:
            break

# Step 5: Print the maximum profit to standard output
print(max_profit)
