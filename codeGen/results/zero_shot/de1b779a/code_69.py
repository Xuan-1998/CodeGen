import sys

n, m, c0, d0 = map(int, input().split())
profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())

    # Check if there's enough dough and stuffing to make at least one bun
    if n >= ci and sum([ai // bi for _ in range(min(n // ci, ai // bi))]) >= min(n // ci, ai // bi):
        # Calculate the maximum number of buns that can be made with this stuffing type
        num_buns = min(n // ci, ai // bi)
        
        # Add up the profits for all the buns that can be made
        profit += di * num_buns

print(profit)
