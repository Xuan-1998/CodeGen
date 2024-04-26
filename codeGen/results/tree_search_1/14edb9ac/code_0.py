from collections import defaultdict
import sys

def dfs(vertex, parent, company, adjacency_list, edge_assignment):
    next_company = 1 if company == 2 else 2  # Alternate between company 1 and 2
    for neighbor, edge_index in adjacency_list[vertex]:
        if neighbor == parent:
            continue
        edge_assignment[edge_index] = company
        dfs(neighbor, vertex, next_company, adjacency_list, edge_assignment)

def solve(n, edges):
    adjacency_list = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adjacency_list[u].append((v, i))
        adjacency_list[v].append((u, i))

    edge_assignment = [0] * (n - 1)
    dfs(1, -1, 1, adjacency_list, edge_assignment)  # Start DFS from vertex 1

    # Count the number of edges assigned to each company
    company_count = defaultdict(int)
    for company in edge_assignment:
        company_count[company] += 1

    # Find the maximum number of edges assigned to a single company
    max_edges = max(company_count.values())

    # Output the result
    print(max_edges, *edge_assignment)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        edges = []
        for _ in range(n - 1):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
        solve(n, edges)

if __name__ == "__main__":
    main()
