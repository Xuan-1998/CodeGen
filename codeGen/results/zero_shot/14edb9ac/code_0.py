from collections import defaultdict

def assign_companies(n, edges):
    # Create an adjacency list for the tree
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    # Initialize variables
    company_assignments = [0] * (n - 1)
    max_company_usage = 0
    company = 1

    # DFS function to assign companies
    def dfs(vertex, parent):
        nonlocal company, max_company_usage
        # Assign companies to the child edges
        for child in tree[vertex]:
            if child != parent:
                global_edge_index = edges.index((min(vertex, child), max(vertex, child)))
                company_assignments[global_edge_index] = company
                company = company % 10**6 + 1
                dfs(child, vertex)

    # Start DFS from vertex 1 (considering it as the root)
    dfs(1, -1)

    # Calculate the maximum number of edges assigned to any company
    max_company_usage = max(company_assignments.count(i) for i in set(company_assignments))

    return max_company_usage, company_assignments

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    # Read number of vertices
    n = int(input().strip())
    # Read edges
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((min(u, v), max(u, v)))  # Store edges in a sorted tuple

    # Assign companies and output the result
    max_usage, assignments = assign_companies(n, edges)
    print(max_usage, *assignments)
