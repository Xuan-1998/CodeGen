from collections import defaultdict
import sys

def assign_companies(n, edges):
    # Initialize adjacency list
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    # Initialize the company assignments and the number of edges per company
    edge_assignment = [-1] * (n - 1)
    company_usage = defaultdict(int)

    def dfs(vertex, parent, company):
        # Assign companies to edges and use DFS to traverse the tree
        for neighbor in adjacency_list[vertex]:
            if neighbor == parent:
                continue
            edge_index = edges.index((min(vertex, neighbor), max(vertex, neighbor)))
            edge_assignment[edge_index] = company
            company_usage[company] += 1
            # Alternate between two companies
            next_company = 3 - company if adjacency_list[neighbor] else company
            dfs(neighbor, vertex, next_company)

    # Start DFS from vertex 1 using company 1
    dfs(1, -1, 1)

    # Find the maximum number of edges assigned to a single company
    max_edges = max(company_usage.values())
    return max_edges, edge_assignment

# Read input from stdin
input_data = sys.stdin.readlines()
line_index = 0
T = int(input_data[line_index].strip())  # Number of test cases
line_index += 1

for _ in range(T):
    n = int(input_data[line_index].strip())  # Number of vertices in the tree
    line_index += 1
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input_data[line_index].strip().split())
        edges.append((min(u, v), max(u, v)))  # Store edges in a sorted tuple
        line_index += 1

    # Solve the problem for the given tree
    max_edges, edge_assignment = assign_companies(n, edges)

    # Output the result to stdout
    print(max_edges, *edge_assignment)
