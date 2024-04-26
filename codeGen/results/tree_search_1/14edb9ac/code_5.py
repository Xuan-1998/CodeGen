from collections import defaultdict
import sys

def dfs(vertex, parent, company, adjacency_list, edge_assignment):
    next_company = 1
    for neighbor in adjacency_list[vertex]:
        if neighbor == parent:
            continue
        edge_assignment[(vertex, neighbor)] = company
        dfs(neighbor, vertex, next_company, adjacency_list, edge_assignment)
        next_company += 1
        if next_company == company:
            next_company += 1

def solve(n, edges):
    adjacency_list = defaultdict(list)
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    edge_assignment = {}
    dfs(1, -1, 1, adjacency_list, edge_assignment)

    max_assigned = max(edge_assignment.values())
    return max_assigned, edge_assignment

def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        edges = [tuple(map(int, input().split())) for _ in range(n-1)]
        max_assigned, edge_assignment = solve(n, edges)
        print(max_assigned)
        for u, v in edges:
            print(edge_assignment.get((u, v)) or edge_assignment.get((v, u)), end=' ')
        print()

if __name__ == "__main__":
    main()
