import sys

def min_operations(n, parents, ranges):
    # Base case: root has no ancestors, so no operations needed
    if n == 1:
        return 0

    # Initialize minimum number of operations
    ops = 0

    # Iterate over vertices in reverse order (from leaf to root)
    for i in range(n-1, 0, -1):
        # Find the maximum value that needs adjustment
        max_val = max(ranges[i][0], ranges[i][1])

        # Calculate the number of operations needed for this vertex
        ops_needed = max(0, max_val - min(ranges[parents[i]][0], ranges[parents[i]][1]))

        # Add to total number of operations
        ops += ops_needed

    return ops

# Read input from stdin
n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
ranges = []
for _ in range(n):
    l, r = map(int, sys.stdin.readline().split())
    ranges.append((l, r))

# Calculate minimum number of operations
ops = min_operations(n, parents, ranges)

# Print output to stdout
print(ops)
