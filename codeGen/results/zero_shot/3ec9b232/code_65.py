import sys
from math import factorial

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of permutations
total_permutations = factorial(n)

# Count the number of permutations for each element in M
perm_count = 1
for i in range(1, n):
    if m[i] > m[i-1]:
        perm_count *= (i - m.index(m[i-1]))
    else:
        perm_count *= (n - m.index(m[i]))

# Calculate the result modulo 10^9+7
result = total_permutations * perm_count % (10**9 + 7)

print(result)
