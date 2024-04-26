import sys

# Read input from stdin
n = int(input())
coordinates = list(map(int, input().split()))
durabilities = list(map(int, input().split()))

# Initialize the maximum segment length each point can support
max_segment_lengths = [0] * n

# Calculate the maximum segment length each point can support
for i in range(n):
    # The segment length that a point can support is twice its durability
    # because it shares the load with its neighbors
    max_segment_lengths[i] = 2 * durabilities[i]

# Find the longest segment between two consecutive points
longest_segment = 0
for i in range(1, n + 1):
    segment_length = coordinates[i] - coordinates[i - 1]
    longest_segment = max(longest_segment, segment_length)

# The minimum durability required for the new point is the length of the longest segment
min_durability_required = longest_segment

# Print the minimum durability required
print(min_durability_required)
