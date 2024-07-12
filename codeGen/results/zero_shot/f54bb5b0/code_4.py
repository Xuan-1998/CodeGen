python
import sys
input = sys.stdin.read
from collections import defaultdict, deque

def count_pairs_with_distance_k(n, k, edges):
    # Step 1: Build the adjacency list for the tree
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    # Step 2: Initialize the answer and a visited set
    answer = 0
    visited = [False] * (n + 1)
    
    # Step 3: Define a DFS function
    def dfs(node):
        nonlocal answer
        visited[node] = True
        # `dist_count` will keep track of the number of nodes at each distance
        dist_count = [0] * (k + 1)
        dist_count[0] = 1
        
        # Process all children
        for neighbor in tree[node]:
            if not visited[neighbor]:
                child_dist_count = dfs(neighbor)
                # Combine results from the child
                for i in range(k):
                    if i + 1 <= k:
                        answer += dist_count[i] * child_dist_count[k - i - 1]
                # Update dist_count with child's distances
                for i in range(k):
                    if i + 1 <= k:
                        dist_count[i + 1] += child_dist_count[i]
        
        return dist_count
    
    # Step 4: Start DFS from any node, here we start from node 1
    dfs(1)
    
    return answer

# Step 5: Read input
data = input().strip().split()
n = int(data[0])
k = int(data[1])
edges = []
for i in range(n - 1):
    a = int(data[2 + 2 * i])
    b = int(data[3 + 2 * i])
    edges.append((a, b))

# Step 6: Get the result and print it
result = count_pairs_with_distance_k(n, k, edges)
print(result)

