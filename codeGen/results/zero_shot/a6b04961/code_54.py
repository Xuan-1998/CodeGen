from collections import deque

def max_hedgehog_beauty():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    # Initialize graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS to find the longest simple path (tail) in the graph
    queue = deque([(0, 0)])  # (vertex, length of path)
    tail_length = 0
    while queue:
        vertex, path_len = queue.popleft()
        if len(graph[vertex]) == 1:  # If this is the last vertex in a simple path
            if path_len > tail_length:
                tail_length = path_len

    # Calculate the number of spines (edges that have one endpoint in the tail and the other endpoint not in the tail)
    spine_count = sum(1 for u, v in edges if u <= tail_length and v > tail_length)

    return tail_length * spine_count

print(max_hedgehog_beauty())
