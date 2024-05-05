# Let's start by reading the input
import sys
n = int(sys.stdin.readline())
edges = []
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

m = int(sys.stdin.readline())
prime_factors = list(map(int, sys.stdin.readline().split()))
k = 1
for p in prime_factors:
    k *= p

# Now let's think about how to solve this problem...
