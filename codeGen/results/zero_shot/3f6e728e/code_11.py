import sys

def find_sequences(N, M):
    # Sort the radii in ascending order
    upper_radii = sorted([int(x) for x in input().split()])
    lower_radii = sorted([int(x) for x in input().split()])

    # Initialize an empty list to store the counts of X-sequences
    sequence_counts = [0] * (C + 1)

    # Iterate over the upper and lower radii
    for i, u_radius in enumerate(upper_radii):
        for j, l_radius in enumerate(lower_radii):
            # If the current radius is different from the previous one
            if i > 0 and u_radius != upper_radii[i - 1] or j > 0 and l_radius != lower_radii[j - 1]:
                # Increment the count of X-sequences with this radius
                sequence_counts[u_radius] += 1
                sequence_counts[l_radius] += 1

    return [x % (10**9 + 7) for x in sequence_counts]

# Read input and process test cases
T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    print(' '.join(map(str, find_sequences(N, M))))
