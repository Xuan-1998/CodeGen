from collections import deque

def assign_companies(n, edges):
    # Initialize the company assignment list with zeros
    company_assignment = [0] * (n - 1)

    # Create adjacency list for the tree
    adj = [[] for _ in range(n + 1)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Perform BFS starting from the leaves
    queue = deque()
    for i in range(1, n + 1):
        if len(adj[i]) == 1:
            queue.append(i)

    # Keep track of the number of edges assigned to each company
    company_usage = [0] * 1000001

    # Assign companies to edges
    current_company = 1
    while queue:
        vertex = queue.popleft()
        for neighbor, edge_idx in adj[vertex]:
            if company_assignment[edge_idx] == 0:
                company_assignment[edge_idx] = current_company
                company_usage[current_company] += 1
                # Move to the next company for the next edge
                current_company = current_company % 1000000 + 1
                # Remove the edge from the neighbor's adjacency list
                adj[neighbor].remove((vertex, edge_idx))
                if len(adj[neighbor]) == 1:
                    queue.append(neighbor)

    # Calculate the maximum number of edges assigned to a single company
    max_edges = max(company_usage[1:])

    return max_edges, company_assignment

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read number of vertices
    n = int(input())
    # Read the edges
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

    # Assign companies to edges
    max_edges, company_assignment = assign_companies(n, edges)

    # Output the results
    print(max_edges)
    print(*company_assignment)
