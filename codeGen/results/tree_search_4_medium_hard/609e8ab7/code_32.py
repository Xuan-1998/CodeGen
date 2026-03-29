from collections import deque

def min_operations(n, parents, values):
    # Create a dictionary to store the parent-child relationships
    tree = {i: [parent] for i, parent in enumerate(parents, 1)}
    
    # Initialize a queue with the leaf nodes (vertices without children)
    queue = deque([i for i in range(2, n+1) if not tree[i]])
    
    # Initialize a dictionary to store the minimum operations required for each vertex
    dp = {i: float('inf') for i in range(n+1)}
    
    while queue:
        node = queue.popleft()
        
        # Update the minimum operations required for this node
        for val, r in zip(values[node-1], values[node]):
            if r - val > 0:
                dp[node] = min(dp[node], dp[parents[node-1]] + (r - val))
    
    return sum(operations - value + r for value, r, operations in zip(*values) if operations != 0)
