from collections import defaultdict

def count_trees(n, parents):
    # Initialize an adjacency list with default values as 0
    adj_list = defaultdict(list)
    
    # Populate the adjacency list using the parent relationships
    for i in range(1, n + 1):
        adj_list[parents[i - 1]].append(i)
    
    # Initialize the count of trees and visited set
    tree_count = 0
    visited = set()
    
    # Iterate through each vertex and perform DFS traversal
    for i in range(1, n + 1):
        if i not in visited:
            stack = [i]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(adj_list[node])
            tree_count += 1
    
    return tree_count

# Example usage
n = int(input())
parents = list(map(int, input().split()))
print(count_trees(n, parents))
