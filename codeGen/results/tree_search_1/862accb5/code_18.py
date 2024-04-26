import sys
from collections import defaultdict

# Read the number of towns (and roads, since they are equal)
n = int(input().strip())

# Initialize an adjacency list to represent the tree
tree = defaultdict(list)

# Read the road information and build the tree
for _ in range(n):
    u, v, l = map(int, input().strip().split())
    tree[u].append((v, l))
    tree[v].append((u, l))

# Function to perform post-order traversal and calculate the subtree sizes
def post_order(node, parent):
    subtree_size = 1  # Count the current node
    max_subtree = 0   # Maximum subtree size after removing a road connected to this node
    for neighbor, road_length in tree[node]:
        if neighbor != parent:
            size_of_subtree, max_size_subtree = post_order(neighbor, node)
            subtree_size += size_of_subtree
            max_subtree = max(max_subtree, size_of_subtree)
            # Update the minimum inconvenience encountered so far
            nonlocal min_inconvenience
            # The inconvenience is the product of the sizes of the two subtrees times the road length
            inconvenience = road_length * size_of_subtree * (n - size_of_subtree)
            min_inconvenience = min(min_inconvenience, inconvenience)
    return subtree_size, max_subtree

# Initialize minimum inconvenience with a large number
min_inconvenience = sys.maxsize

# Perform post-order traversal starting from node 1 (assuming 1 is always part of the tree)
post_order(1, -1)

# Output the minimum possible inconvenience
print(min_inconvenience)
