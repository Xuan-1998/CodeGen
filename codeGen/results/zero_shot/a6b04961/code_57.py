import sys
from collections import defaultdict

def find_max_beauty(n, m, edges):
    # Build an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find all possible tails in the graph (i.e., all simple paths)
    max_tail_length = 0
    tails = []
    for start in range(n):
        for end in range(start + 1, n):
            path = [start]
            current = start
            while current < end:
                next_node = None
                for neighbor in graph[current]:
                    if neighbor not in path and neighbor < end:
                        next_node = neighbor
                        break
                if next_node is None:
                    break
                path.append(next_node)
                current = next_node
            if len(path) > max_tail_length:
                max_tail_length = len(path)
                tails = [path]
            elif len(path) == max_tail_length:
                tails.append(path)

    # For each tail, count the number of spines (edges that have one endpoint in the tail and the other endpoint not in the tail)
    max_beauty = 0
    for tail in tails:
        spine_count = 0
        for edge in edges:
            if edge[0] in tail and edge[1] not in tail:
                spine_count += 1
            elif edge[1] in tail and edge[0] not in tail:
                spine_count += 1
        max_beauty = max(max_beauty, len(tail) * spine_count)

    return max_beauty

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

# Calculate the maximum possible beauty of a hedgehog
max_beauty = find_max_beauty(n, m, edges)

# Print the answer to stdout
print(max_beauty)
