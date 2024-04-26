from collections import defaultdict, deque
import sys

def find_longest_path(graph, in_degree, n):
    # Perform topological sort using Kahn's algorithm
    topo_order = []
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # If topo_order does not contain all nodes, there's a cycle
    if len(topo_order) != n:
        return -1

    # Find the longest path using dynamic programming
    longest_path = [0] * n
    for u in topo_order:
        for v in graph[u]:
            longest_path[v] = max(longest_path[v], longest_path[u] + 1)
    return max(longest_path) + 1

def solve(test_cases):
    results = []
    for n, graph in test_cases:
        in_degree = [0] * n
        for u in range(n):
            for v in graph[u]:
                in_degree[v] += 1
        result = find_longest_path(graph, in_degree, n)
        results.append(result)
    return results

def read_input():
    test_cases = []
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        graph = defaultdict(list)
        for i in range(n):
            line = list(map(int, input().strip().split()))
            k_i = line[0]
            for j in range(1, k_i + 1):
                graph[i].append(line[j] - 1)  # Convert to 0-based indexing
        test_cases.append((n, graph))
    return test_cases

def main():
    test_cases = read_input()
    results = solve(test_cases)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
