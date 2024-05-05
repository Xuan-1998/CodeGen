from collections import deque

def can_cross_stones(stones):
    n = len(stones)
    graph = [[] for _ in range(n + 1)]
    
    # Construct the graph
    for i, (x, y) in enumerate(zip([0] + stones, stones + [n])):
        for j in range(i - 1, min(i + 2, n)):
            if abs(x - stones[j]) in [abs(k - 1), k, abs(k + 1)]:
                graph[x].append(y)
                graph[y].append(x)

    # Perform BFS
    visited = set()
    queue = deque([0])
    while queue:
        node = queue.popleft()
        if node == n:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append(neighbor)
    return False

# Read input from stdin
stones = [int(x) for x in input().split()]

# Print the answer to stdout
print(can_cross_stones(stones))
