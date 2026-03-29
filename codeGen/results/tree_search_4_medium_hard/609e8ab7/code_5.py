import heapq

def min_operations(n, parents, ranges):
    # Create a dictionary to store the memoized values
    memo = {i: 0 for i in range(1, n+1)}

    # Initialize a priority queue with all leaf nodes
    pq = [(0, i) for i in range(1, n)]
    heapq.heapify(pq)

    while pq:
        # Extract the node with the minimum number of operations from the priority queue
        curr_ops, node = heapq.heappop(pq)

        # For each child node of this extracted node
        if parents[node]:
            child_node = parents[node]
            new_ops = curr_ops + (ranges[child_node][1] - ranges[child_node][0]) + memo[child_node]

            # Store the updated value in our memoization table and add it to the priority queue if necessary
            memo[node] = new_ops
            heapq.heappush(pq, (new_ops, node))

    return [memo[i] for i in range(1, n+1)]

# Test your code here
n = 5  # Number of vertices
parents = [0, 2, 2, 4, 4]  # Parent nodes
ranges = [(1, 3), (1, 3), (2, 4), (2, 4), (3, 5)]  # Ranges for each node

# Output: The minimum number of operations needed to adjust all vertices to their respective ranges.
print(min_operations(n, parents, ranges))
