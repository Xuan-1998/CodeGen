def read_graph():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append([u-1, v-1])
        graph[v-1].append([v-1, u-1])

    return graph

def max_hedgehog_beauty(graph):
    # Initialize variables
    max_beauty = 0
    max_tail_length = 0

    for start_vertex in range(len(graph)):
        visited = set()
        stack = [(start_vertex, [start_vertex])]

        while stack:
            current_vertex, path = stack.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)

                # Check if the path is a simple path
                if len(path) > max_tail_length:
                    max_tail_length = len(path)

                # Count spines for this path
                spine_count = 0
                for edge in graph[current_vertex]:
                    if edge[1] not in visited:
                        spine_count += 1

                max_beauty = max(max_beauty, max_tail_length * spine_count)

    return max_beauty

graph = read_graph()
print(max_hedgehog_beauty(graph))
