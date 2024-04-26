from collections import defaultdict, deque
import sys

def assign_companies(n, edges):
    # Create an adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Initialize variables
    edge_assignment = [-1] * (n - 1)
    company_usage = defaultdict(int)
    max_edges = 0
    company = 1

    # BFS traversal
    visited = [False] * (n + 1)
    queue = deque([1])
    visited[1] = True

    while queue:
        current = queue.popleft()
        used_companies = set()

        for neighbor in adj[current]:
            if visited[neighbor]:
                continue
            visited[neighbor] = True
            queue.append(neighbor)

            # Assign the company to the current edge
            while company in used_companies:
                company = 1 if company == 10**6 else company + 1

            # Find the index of the edge in the original list
            edge_index = edges.index((min(current, neighbor), max(current, neighbor)))
            edge_assignment[edge_index] = company
            used_companies.add(company)
            company_usage[company] += 1
            max_edges = max(max_edges, company_usage[company])

            # Update the company for the next edge
            company = 1 if company == 10**6 else company + 1

    return max_edges, edge_assignment

# Read input
input_data = sys.stdin.readlines()
test_cases = int(input_data[0])
line_idx = 1

for _ in range(test_cases):
    n = int(input_data[line_idx])
    line_idx += 1
    edges = []

    for _ in range(n - 1):
        u, v = map(int, input_data[line_idx].split())
        line_idx += 1
        edges.append((min(u, v), max(u, v)))

    # Solve the test case
    max_edges, edge_assignment = assign_companies(n, edges)

    # Output the result
    print(max_edges)
    print(' '.join(map(str, edge_assignment)))
