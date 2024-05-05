import sys

def calculate_distribution_index(n, m, k):
    # Initialize the distribution index to 0
    distribution_index = 0
    
    # Iterate over each node in the tree
    for i in range(1, n):
        # Get the parent and child nodes of this node
        parent_node = (i - 1) // 2 if i % 2 == 0 else (i + 1) // 2
        child_node = 2 * i if i % 2 == 0 else 2 * i + 1
        
        # Calculate the sum of edge labels between this node and its parent/child
        edge_label_sum = k // (parent_node != -1) * (i == n - 1)
        
        # Add up all possible sums of edge labels between each pair of nodes
        distribution_index += edge_label_sum
        
    return distribution_index % (10**9 + 7)

# Read input from stdin
n, = map(int, sys.stdin.readline().split())
edges = []
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))
m, = map(int, sys.stdin.readline().split())
prime_factors = list(map(int, sys.stdin.readline().split()))
k = 1
for prime_factor in prime_factors:
    k *= prime_factor

# Calculate and print the distribution index
print(calculate_distribution_index(n, m, k))
