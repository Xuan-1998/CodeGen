import sys

# Read input from standard input
N, M, C = map(int, sys.stdin.readline().split())
upper_radii = list(map(int, sys.stdin.readline().split()))
lower_radii = list(map(int, sys.stdin.readline().split()))

counts = [0] * (C + 1)
for i in range(C):
    upper_count = sum(1 for u in upper_radii if u <= i)
    lower_count = sum(1 for l in lower_radii if l >= i)
    counts[i] = (counts[i-1] + upper_count * lower_count) % (10**9 + 7)

# Print output
print(' '.join(map(str, counts)))
