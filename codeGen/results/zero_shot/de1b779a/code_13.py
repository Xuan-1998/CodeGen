import sys

n, m, c0, d0 = map(int, input().split())
profit = 0

for _ in range(m):
    ai, bi, ci, di = map(int, input().split())
    
    # Calculate the maximum number of buns that can be made with this stuffing
    num_buns = min(c0 // ci, ai // bi)
    
    # Update the remaining dough and stuffing
    c0 -= num_buns * ci
    ai -= num_buns * bi
    
    # Add the profit from selling these buns to the total profit
    profit += num_buns * di

print(profit)
