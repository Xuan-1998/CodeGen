from collections import defaultdict

def dfs(current, parent, companies, edges, company_assignment):
    # Start with the first company
    company_index = 0
    for neighbor in edges[current]:
        if neighbor != parent:
            # Assign the company to the edge
            company_assignment[(min(current, neighbor), max(current, neighbor))] = companies[company_index]
            # Alternate between the two companies
            company_index = 1 - company_index
            # Continue DFS with the next neighbor
            dfs(neighbor, current, companies, edges, company_assignment)

def solve_tree(n, edge_list):
    # Initialize the adjacency list for the tree
    edges = defaultdict(list)
    for u, v in edge_list:
        edges[u].append(v)
        edges[v].append(u)

    # Initialize company assignment for each edge (using a tuple to represent an edge)
    company_assignment = {}
    # Perform DFS starting from node 1
    dfs(1, -1, [1, 2], edges, company_assignment)

    # Find the maximum number of edges assigned to a single company
    company_usage = defaultdict(int)
    for company in company_assignment.values():
        company_usage[company] += 1
    max_edges = max(company_usage.values())

    # Output the result
    print(max_edges)
    for u, v in edge_list:
        print(company_assignment[(min(u, v), max(u, v))], end=' ')
    print()

# Read input and process each test case
T = int(input())
for _ in range(T):
    n = int(input())
    edge_list = [tuple(map(int, input().split())) for _ in range(n - 1)]
    solve_tree(n, edge_list)
