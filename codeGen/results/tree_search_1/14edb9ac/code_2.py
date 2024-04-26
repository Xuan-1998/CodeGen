from collections import defaultdict
import sys

def dfs(node, parent, graph, edge_companies, company_usage):
    companies_used = set()
    if parent != -1:  # If it's not the root, add the parent's company to the used set
        companies_used.add(edge_companies[(min(node, parent), max(node, parent))])
    
    company = 1
    for child in graph[node]:
        if child == parent:
            continue
        # Find the next available company that's not used by the parent or sibling
        while company in companies_used:
            company += 1
        # Assign the company to the current edge
        edge_companies[(min(node, child), max(node, child))] = company
        companies_used.add(company)
        company_usage[company] += 1
        # Recurse on the child
        dfs(child, node, graph, edge_companies, company_usage)

def solve(n, edges):
    graph = defaultdict(list)
    edge_companies = {}
    company_usage = defaultdict(int)
    
    # Build the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Perform a DFS post-order traversal
    dfs(1, -1, graph, edge_companies, company_usage)
    
    # Find the maximum number of edges assigned to a single company
    max_edges = max(company_usage.values())
    
    # Output the result
    print(max_edges)
    for u, v in edges:
        print(edge_companies[(min(u, v), max(u, v))], end=' ')
    print()

# Read input from stdin
input_lines = sys.stdin.readlines()
current_line = 0

# Number of test cases
T = int(input_lines[current_line].strip())
current_line += 1

for _ in range(T):
    # Number of vertices
    n = int(input_lines[current_line].strip())
    current_line += 1
    
    # Edges of the tree
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input_lines[current_line].strip().split())
        current_line += 1
        edges.append((u, v))
    
    # Solve the current test case
    solve(n, edges)
