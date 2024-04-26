import sys

def find_min_durability(n, coords, durability):
    # Calculate initial loads (distances to the next point)
    loads = [coords[i+1] - coords[i] for i in range(n+1)]

    # Prefix sums for loads on the points from the left
    prefix_sums = [0] * (n + 2)
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i-1] + loads[i-1]

    # Suffix sums for loads on the points from the right
    suffix_sums = [0] * (n + 2)
    for i in range(n, 0, -1):
        suffix_sums[i] = suffix_sums[i+1] + loads[i]

    # Find the minimum durability required
    min_durability = 0
    for i in range(1, n + 1):
        # Check if the point can support the load
        if prefix_sums[i] > durability[i-1] or suffix_sums[i] > durability[i-1]:
            # If not, redistribute the load to the neighboring points
            load_to_redistribute = max(prefix_sums[i], suffix_sums[i])
            if i > 1:
                prefix_sums[i-1] += load_to_redistribute // 2
            if i < n:
                suffix_sums[i+1] += load_to_redistribute // 2
            # Update the minimum durability required
            min_durability = max(min_durability, load_to_redistribute)

    return min_durability

# Read input from stdin
n = int(sys.stdin.readline())
coords = list(map(int, sys.stdin.readline().split()))
durability = list(map(int, sys.stdin.readline().split()))

# Calculate and print the answer
answer = find_min_durability(n, coords, durability)
print(answer)
