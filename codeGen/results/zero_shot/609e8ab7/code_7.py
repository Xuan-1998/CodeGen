from collections import deque

def min_operations(node_values):
    n = len(node_values)
    tree = [[] for _ in range(n)]
    
    # Process edges
    for i, edge in enumerate(sys.stdin.readline().split()):
        tree[edge[0]].append((i + 1, int(edge[1])))

    # Initialize queue and visited set
    queue = deque([0])
    visited = {0}

    while queue:
        node = queue.popleft()
        
        # Process node values for the current node
        if (node_values[node][0] > node_values[node][1]):
            diff = abs(node_values[node][0] - node_values[node][1]) + 1
            node_values[node][0] -= diff // 2
            node_values[node][1] += diff // 2

        # Process children
        for child, parent in tree[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return sum(node[1] - node[0] + 1 for node in node_values)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    node_values = [map(int, sys.stdin.readline().split()) for _ in range(n)]
    print(min_operations(node_values))
