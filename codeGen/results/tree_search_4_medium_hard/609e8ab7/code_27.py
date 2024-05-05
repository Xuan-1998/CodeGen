import sys
from collections import deque

# Input the number of test cases
T = int(input())

for _ in range(T):
    # Read the number of vertices
    n = int(input())
    
    # Read the parent-child relationships
    parents = list(map(int, input().split()))
    
    # Initialize the dp table with infinity values
    dp = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    
    # Read the ranges for each vertex
    ranges = []
    for i in range(1, n + 1):
        l, r = map(int, input().split())
        ranges.append((l, r))
    
    # Initialize the queue with the root node (vertex 1)
    queue = deque([(1, 0)])
    
    while queue:
        vertex, operations = queue.popleft()
        
        # If this is not the first operation for this vertex
        if dp[vertex][operations] != sys.maxsize:
            continue
        
        # If the value of this vertex is within its range
        if ranges[vertex - 1][0] <= operations <= ranges[vertex - 1][1]:
            dp[vertex][operations] = 0
        else:
            # Calculate the minimum number of operations needed for this vertex
            for i in range(1, n + 1):
                if parents[i - 1] == vertex and i != 1:
                    queue.append((i, operations))
    
    # Print the minimum number of operations needed for the root node
    print(min(dp[1]))
