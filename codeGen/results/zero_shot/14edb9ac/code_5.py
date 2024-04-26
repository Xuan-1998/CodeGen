import sys
from collections import defaultdict, deque

def assign_companies(n, edges):
    # Create an adjacency list for the tree
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize company assignments and visited array
    company_assignment = [-1] * (n - 1)
    visited = [False] * (n + 1)

    # Start BFS from the root node (1)
    queue = deque([1])
    visited[1] = True

    # Company numbers to be used
    companies = [1, 2]
    company_index = 0

    while queue:
        vertex = queue.popleft()
        # Alternate between two companies
        company = companies[company_index]
        company_index ^= 1  # Toggle between 0 and 1

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                # Assign the current company to the edge
                edge_index = edges.index((min(vertex, neighbor), max(vertex, neighbor)))
                company_assignment[edge_index] = company

    # Calculate the maximum number of edges assigned to a single company
    max_edges = max(company_assignment.count(1), company_assignment.count(2))
    return max_edges, company_assignment

# Read input and process each test case
def main():
    input_data = sys.stdin.readlines()
    line_index = 0
    t = int(input_data[line_index].strip())  # Number of test cases
    line_index += 1

    for _ in range(t):
        n = int(input_data[line_index].strip())  # Number of vertices
        line_index += 1
        edges = []
        for _ in range(n - 1):
            u, v = map(int, input_data[line_index].strip().split())
            edges.append((min(u, v), max(u, v)))
            line_index += 1

        max_edges, company_assignment = assign_companies(n, edges)
        print(max_edges, *company_assignment)

if __name__ == "__main__":
    main()
