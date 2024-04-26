from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def assign_companies(n, edges):
    # Initialize company assignment for each edge
    companies = [0] * (n - 1)
    # Adjacency list for the tree
    graph = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        graph[u].append((v, i))
        graph[v].append((u, i))
    
    def dfs(node, parent, company):
        # Assign companies to edges in a DFS manner
        next_company = 1
        for neighbor, edge_index in graph[node]:
            if neighbor == parent:
                continue
            if next_company == company:
                next_company += 1
            companies[edge_index] = next_company
            dfs(neighbor, node, next_company)
            next_company += 1
    
    # Start DFS from the first node with an arbitrary company
    dfs(1, -1, 0)
    max_assigned = max(companies)
    return max_assigned, companies

def main():
    # Read number of test cases
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
        max_assigned, company_assignments = assign_companies(n, edges)
        print(max_assigned)
        print(' '.join(map(str, company_assignments)))

if __name__ == "__main__":
    main()
