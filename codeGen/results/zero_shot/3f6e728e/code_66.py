import sys
from collections import defaultdict

# Read input
T = int(sys.stdin.readline())
for _ in range(T):
    N, M, C = map(int, sys.stdin.readline().split())
    upper_radii = list(map(int, sys.stdin.readline().split()))
    lower_radii = list(map(int, sys.stdin.readline().split()))

    # Create a dictionary to store the count of each radius
    radius_count = defaultdict(int)
    for r in upper_radii:
        radius_count[r] += 1
    for r in lower_radii:
        radius_count[r] += 1

    # Calculate the number of ways to build each X-sequence length
    x_sequence_counts = [0] * (C + 1)
    for i in range(C + 1):
        x_sequence_counts[i] = (radius_count[i] + 1) if radius_count.get(i, 0) > 0 else 0

    # Print the result
    print(' '.join(map(str, x_sequence_counts)))
