from collections import defaultdict, deque
import sys

def topological_sort(graph, in_degree):
    # Perform Kahn's Algorithm for topological sorting
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return topo_order

def min_reads(graph, in_degree, n):
    topo_order = topological_sort(graph, in_degree)
    if len(topo_order) != n:
        return -1  # The graph is not a DAG, so it's impossible to read the book

    dp = [0] * (n + 1)
    for node in topo_order:
        for neighbor in graph[node]:
            dp[neighbor] = max(dp[neighbor], dp[node] + 1)
    return max(dp) + 1

def main():
    input_data = sys.stdin.readlines()
    line_index = 0
    while line_index < len(input_data):
        n = int(input_data[line_index].strip())
        line_index += 1
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        for i in range(1, n + 1):
            parts = list(map(int, input_data[line_index].strip().split()))
            line_index += 1
            k_i = parts[0]
            prerequisites = parts[1:]
            for prereq in prerequisites:
                graph[prereq].append(i)
                in_degree[i] += 1

        # If a node has no incoming edges, set its in_degree to 0
        for i in range(1, n + 1):
            in_degree.setdefault(i, 0)

        result = min_reads(graph, in_degree, n)
        print(result)

if __name__ == "__main__":
    main()
