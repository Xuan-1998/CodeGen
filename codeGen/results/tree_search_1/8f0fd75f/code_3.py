import sys

# Read input from stdin
n = int(input().strip())
coordinates = list(map(int, input().strip().split()))
durabilities = list(map(int, input().strip().split()))

# Initialize prefix and suffix arrays
prefix_max_load = [0] * (n + 1)
suffix_max_load = [0] * (n + 1)

# Calculate initial load on each ordinary point
for i in range(1, n + 1):
    prefix_max_load[i] = coordinates[i] - coordinates[i - 1]
for i in range(n - 1, -1, -1):
    suffix_max_load[i] = coordinates[i + 1] - coordinates[i]

# Update prefix and suffix max loads considering the durability of points
for i in range(1, n + 1):
    prefix_max_load[i] = min(prefix_max_load[i], prefix_max_load[i - 1] + durabilities[i - 1])
for i in range(n - 1, -1, -1):
    suffix_max_load[i] = min(suffix_max_load[i], suffix_max_load[i + 1] + durabilities[i])

# Find the minimum durability required for an additional point
min_durability = 0
for i in range(n):
    # The load that needs to be supported by the new point
    load = prefix_max_load[i] + suffix_max_load[i + 1]
    if load > durabilities[i]:
        min_durability = max(min_durability, load - durabilities[i])

# Print the result
print(min_durability)
