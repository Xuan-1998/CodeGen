import sys

# Read input from stdin
t, l, r = map(int, input().split())

# Initialize variables
total = 0
for i in range(t):
    total += (10**i) * f(l + i)

total -= l * f(r)

print(total % (10**9 + 7))

