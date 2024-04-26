import sys
from collections import defaultdict

MOD = 998244353

# Function to check if the tree is a caterpillar tree and count permutations
def count_caterpillar_permutations(n, edges):
    # Build the adjacency list
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Check if the tree is a caterpillar tree
    # A tree is a caterpillar tree if all but at most two vertices have degree 2 or less
    more_than_two_degree_count = 0
    for node in adjacency_list:
        if len(adjacency_list[node]) > 2:
            more_than_two_degree_count += 1
            if more_than_two_degree_count > 2:
                return 0  # Not a caterpillar tree

    # If it is a caterpillar tree, calculate the permutations
    # For a caterpillar tree, there are (n - 1)! permutations
    permutations = 1
    for i in range(2, n):
        permutations = (permutations * i) % MOD

    return permutations

# Read input from stdin
n = int(sys.stdin.readline().strip())
edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n - 1)]

# Get the number of valid permutations
result = count_caterpillar_permutations(n, edges)

# Print the result to stdout
print(result)
