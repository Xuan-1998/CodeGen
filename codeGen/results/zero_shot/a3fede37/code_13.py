import sys

# Read input array
input_array = [int(x) for x in sys.stdin.readline().split()]

# Parse input array into a binary tree
root = parse_array_to_tree(input_array)

# Find the maximum sum of a path in the tree
max_sum = max_path_sum(root)

# Print output
print(max_sum)
