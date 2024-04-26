from collections import defaultdict
import sys

def pre_order_traversal(graph, node, parent, company, edge_assignment, company_usage):
    # Alternate between company 1 and 2
    next_company = 1 if company == 2 else 2
    for child in graph[node]:
        if child != parent:
            # Assign the company to the edge
            edge_assignment[(min(node, child), max(node, child))] = company
            company_usage[company] += 1
            # Recur for the child node with the next company
            pre_order_traversal(graph, child, node, next_company, edge_assignment, company_usage)

def solve_tree(n, edges):
    # Initialize graph representation
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Dictionary to hold the assigned company for each edge
    edge_assignment = {}
    # Dictionary to track the number of edges assigned to each company
    company_usage = defaultdict(int)
    
    # Start pre-order traversal from node 1 with company 1
    pre_order_traversal(graph, 1, -1, 1, edge_assignment, company_usage)
    
    # Find the maximum number of edges assigned to a single company
    max_edges = max(company_usage.values())
    
    # Prepare the output in the required format
    output_edges = [edge_assignment[(min(u, v), max(u, v))] for u, v in edges]
    return max_edges, output_edges

# Read input from stdin
input_lines = sys.stdin.readlines()
line_index = 0
T = int(input_lines[line_index].strip())
line_index += 1

# Process each test case
for _ in range(T):
    n = int(input_lines[line_index].strip())
    line_index += 1
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input_lines[line_index].strip().split())
        line_index += 1
        edges.append((u, v))
    
    # Solve the problem for the current test case
    max_edges, output_edges = solve_tree(n, edges)
    
    # Print the result to stdout
    print(max_edges)
    print(*output_edges)
