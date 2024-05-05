from collections import deque

def min_operations(n, parents, ranges):
    # Create a graph representation as a dictionary
    graph = {i: [] for i in range(1, n+1)}
    for i in range(2, n+1):
        graph[parents[i-1]].append(i)

    # Initialize the queue with the root node (vertex 1)
    queue = deque([1])

    # Initialize a dictionary to store the minimum number of operations needed
    # for each vertex
    dp = {i: float('inf') for i in range(1, n+1)}

    # Perform topological sorting and dynamic programming
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if ranges[child-1][0] < ranges[child-1][1]:
                dp[child] = min(dp[child], dp[node] + 1)
            queue.append(child)

    # The minimum number of operations needed is the minimum value in the dp dictionary
    return min(dp.values())
