import sys

# Read the input binary tree from stdin
n = int(sys.stdin.readline())
tree = [int(x) for x in sys.stdin.read().split()]

# Calculate and print the maximum sum of a path
print(max_path_sum(tree))
