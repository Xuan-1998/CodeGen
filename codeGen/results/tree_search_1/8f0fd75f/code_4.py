import sys

# Read input from stdin
n = int(input().strip())
coordinates = list(map(int, input().strip().split()))
durabilities = list(map(int, input().strip().split()))

# Calculate the lengths of all segments
segments = [coordinates[i+1] - coordinates[i] for i in range(n+1)]

# Calculate prefix and suffix arrays to keep track of the maximum segment length
prefix_max = [0] * (n + 2)
suffix_max = [0] * (n + 2)

for i in range(1, n+1):
    prefix_max[i] = max(prefix_max[i-1], segments[i-1])

for i in range(n, 0, -1):
    suffix_max[i] = max(suffix_max[i+1], segments[i])

# Iterate through each ordinary point to find the minimum durability required
min_durability_required = 0
for i in range(1, n+1):
    # Check if the point collapses
    if segments[i-1] > durabilities[i-1] or segments[i] > durabilities[i-1]:
        # Calculate the max segment length it would need to support
        max_length_supported = max(prefix_max[i], suffix_max[i])
        min_durability_required = max(min_durability_required, max_length_supported)

# If no ordinary points collapse, we don't need to add a new point
if min_durability_required == 0:
    for i in range(1, n+1):
        if segments[i-1] <= durabilities[i-1] and segments[i] <= durabilities[i-1]:
            print(0)
            sys.exit()

# Print the minimum durability required for a new ordinary point
print(min_durability_required)
