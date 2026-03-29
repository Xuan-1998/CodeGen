import sys
from collections import defaultdict

def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # Step 1: Find all connected components
    visited = [False] * (n + 1)
    component_sizes = []

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for neighbor in graph[node]:
                dfs(neighbor)

    for node in range(1, n + 1):
        if not visited[node]:
            component_sizes.append(len(list(dfs(node))))
            visited[node] = True

    # Step 2: Find the maximum beauty possible
    max_beauty = 0

    def calculate_beauty(tail_length, spine_count):
        nonlocal max_beauty
        max_beauty = max(max_beauty, tail_length * spine_count)

    for _ in range(len(component_sizes)):
        for i in range(1, len(component_sizes) - 1):
            tail_length = component_sizes[i]
            spine_count = sum([component_sizes[j] for j in range(len(component_sizes)) if j != i])
            calculate_beauty(tail_length, spine_count)

    print(max_beauty)

if __name__ == "__main__":
    solve()
