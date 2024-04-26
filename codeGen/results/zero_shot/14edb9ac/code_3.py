from collections import defaultdict
import sys

# Function to assign companies to edges
def assign_companies(n, edges):
    # Initialize the adjacency list
    adj_list = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj_list[u].append((v, i))
        adj_list[v].append((u, i))

    # Initialize the result array with -1
    result = [-1] * (n - 1)
    # Start with company 1
    company = 1

    # Depth-first search to assign companies
    def dfs(node, parent):
        nonlocal company
        # Assign companies to edges
        for neighbor, edge_index in adj_list[node]:
            if neighbor == parent:
                continue
            if result[edge_index] == -1:  # If the edge is not assigned yet
                result[edge_index] = company
                # Rotate the company assignment
                company = company % 10**6 + 1
                dfs(neighbor, node)

    # Start DFS from node 1
    dfs(1, -1)
    # Calculate the maximum number of edges assigned to a single company
    max_edges = max(result.count(i) for i in range(1, 10**6 + 1))
    return max_edges, result

# Read the number of test cases
T = int(sys.stdin.readline().strip())

# Process each test case
for _ in range(T):
    # Read the number of vertices
    n = int(sys.stdin.readline().strip())
    # Read the edges
    edges = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n - 1)]
    # Assign companies and get the result
    max_edges, assignment = assign_companies(n, edges)
    # Print the result
    print(max_edges, *assignment)
