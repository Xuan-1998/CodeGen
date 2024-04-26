# Function to perform DFS and find the farthest node, its distance, and the edge to remove
def dfs(node, parent):
    farthest_node = (node, 0)
    max_length_in_subtree = 0
    for neighbor, length in roads[node]:
        if neighbor != parent:
            next_node, dist = dfs(neighbor, node)
            dist += length
            max_length_in_subtree = max(max_length_in_subtree, dist)
            if dist > farthest_node[1]:
                farthest_node = (next_node, dist)
    return farthest_node, max_length_in_subtree

# Perform two DFS to find the diameter of the tree and the edge to remove
farthest_from_root = dfs(1, -1)[0]
diameter_endpoints, max_length = dfs(farthest_from_root, -1)

# Find the edge to remove by minimizing the maximum distance of the two resulting subtrees
min_inconvenience = max_length
print(min_inconvenience)
