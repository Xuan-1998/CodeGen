import sys

# Read input from stdin
n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffs = []
for i in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffs.append((ai, bi, ci, di))

# Initialize variables
max_profit = 0

# Iterate over all possible combinations of buns
for bun_config in itertools.product(range(m+1), repeat=n):
    profit = 0
    dough_left = n
    stuffing_left = [a for a, _ in stuffs]
    for i, (dough_used, stuffing_used) in enumerate(bun_config):
        if dough_used > 0:
            dough_left -= c0 + ci * min(dough_used, sum(stuffing_left))
        if stuffing_used > 0:
            for j, (ai, bi, ci, di) in enumerate(stuffs):
                if ai > 0 and stuffing_used <= bi:
                    ai -= bi
                    profit += di * min(dough_used, bi)
                    break
    max_profit = max(max_profit, profit)

# Print the result to stdout
print(max_profit)
