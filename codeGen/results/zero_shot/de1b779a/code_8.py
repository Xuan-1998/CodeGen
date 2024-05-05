import sys
from scipy.optimize import linprog

# Read input from stdin
n, m, c0, d0 = map(int, sys.stdin.readline().split())
stuffings = []
for _ in range(m):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    stuffings.append((ai, bi, ci, di))

# Define the coefficients for the profit function
coeffs = [0] * (m + 1)
for i in range(m):
    coeffs[i] = -di
coeffs[m] = d0

# Define the bounds for the decision variables
bounds = [(0, n) for _ in range(m)] + [(0, n)]
bounds[-1][1] = m  # Make sure we don't make more than m buns without any stuffing

# Solve the linear programming problem
res = linprog(coeffs, stuffings)

# Print the maximum profit to stdout
print(int(res.fun))
