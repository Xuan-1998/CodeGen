from collections import defaultdict

def dfs(tree, node, parent, company, edge_assignment):
    current_company = 1
    for neighbor in tree[node]:
        if neighbor == parent:
            continue
        if current_company == company:
            current_company += 1
        edge_assignment[(node, neighbor)] = current_company
        edge_assignment[(neighbor, node)] = current_company
        dfs(tree, neighbor, node, current_company, edge_assignment)
        current_company += 1

def solve(test_cases):
    results = []
    for n, edges in test_cases:
        tree = defaultdict(list)
        edge_assignment = {}
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Start DFS from node 1, with no parent and initial company 1
        dfs(tree, 1, -1, 0, edge_assignment)
        
        # Find the minimum possible number of edges assigned to the most used company
        max_edges_assigned = max(edge_assignment.values())
        company_assignment = [edge_assignment[tuple(edge)] for edge in edges]
        
        results.append((max_edges_assigned, company_assignment))
    
    return results

# Read input from stdin
def read_input():
    t = int(input().strip())  # Number of test cases
    test_cases = []
    for _ in range(t):
        n = int(input().strip())
        edges = [tuple(map(int, input().split())) for _ in range(n-1)]
        test_cases.append((n, edges))
    return test_cases

# Output results to stdout
def print_output(results):
    for max_edges_assigned, company_assignment in results:
        print(max_edges_assigned)
        print(' '.join(map(str, company_assignment)))

# Main execution
if __name__ == "__main__":
    test_cases = read_input()
    results = solve(test_cases)
    print_output(results)
