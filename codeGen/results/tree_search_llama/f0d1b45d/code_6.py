import sys

def count_trees(relatives):
    n = int(sys.stdin.readline())
    rels = list(map(int, sys.stdin.readline().split()))
    
    # Create an adjacency list representation of the graph
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n-1):
        a, b = rels[i], rels[i+1]
        graph[a].append(b)
        graph[b].append(a)

    # Perform BFS to find connected components
    trees = 0
    visited = set()
    for node in range(n):
        if node not in visited:
            queue = [node]
            while queue:
                current_node = queue.pop(0)
                if current_node not in visited:
                    visited.add(current_node)
                    for neighbor in graph[current_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            trees += 1

    return trees

print(count_trees(sys.stdin.readline()))
