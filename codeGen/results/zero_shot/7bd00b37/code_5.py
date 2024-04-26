def find_centroid(edges, n):
    size = [1] * (n + 1)
    max_subtree = [0] * (n + 1)
    visited = [False] * (n + 1)
    to_visit = deque([1])
    visited[1] = True

    # First DFS to compute the size of each subtree
    while to_visit:
        node = to_visit[-1]
        if all(visited[nei] for nei in edges[node]):
            to_visit.pop()
            for nei in edges[node]:
                if nei != node:  # Avoid counting the node itself
                    size[node] += size[nei]
                    max_subtree[node] = max(max_subtree[node], size[nei])
        else:
            for nei in edges[node]:
                if not visited[nei]:
                    visited[nei] = True
                    to_visit.append(nei)

    # Find the centroid(s)
    for node in range(1, n + 1):
        max_subtree[node] = max(max_subtree[node], n - size[node])  # Consider the "outside" subtree
        if max_subtree[node] <= n // 2:
            return node

    return -1  # Should not happen if the input is a valid tree
