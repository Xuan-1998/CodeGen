from collections import defaultdict

def max_hedgehog_bauty(n, m, edges):
    # Build graph using adjacency list representation
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform DFS to find the longest possible simple path (tail)
    tail_length = 0
    visited = set()
    current_vertex = None
    for vertex in range(1, n+1):
        if vertex not in visited:
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    if current_vertex is None:
                        current_vertex = v
                    elif v != current_vertex + 1:
                        break
                    else:
                        current_vertex = v
            tail_length += (current_vertex - vertex + 1) if vertex == current_vertex else 0

    # Calculate the number of spines
    spine_count = sum(1 for u, v in edges if u < tail_length and v >= tail_length)

    return tail_length * spine_count


# Read input from standard input
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Calculate the maximum possible beauty of a hedgehog
max_beaauty = max_hedgehog_bauty(n, m, edges)

print(max_beaauty)
