import heapq

def max_hedgehog_beauty(n, m, edges):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize a dynamic programming table and a priority queue
    dp = [0] * (n + 1)
    pq = [(0, 1)]  # (beauty, tail_length)

    while pq:
        beauty, tail_len = heapq.heappop(pq)
        for i in range(tail_len - 1, n):
            # Compute the beauty of extending the current tail with a new vertex
            next_beauty = beauty * (i + 1) + sum(1 for j in range(n) if graph[i][j] and not dp[j])
            # Update the dynamic programming table
            dp[i + 1] = max(dp[i + 1], next_beauty)
            # Add the new tail length to the priority queue
            heapq.heappush(pq, (dp[i + 1], i + 2))

    return dp[-1]

n, m = map(int, input().split())
edges = [(int(i[0]), int(i[1])) for i in [input().split() for _ in range(m)]]
print(max_hedgehog_beauty(n, m, edges))
