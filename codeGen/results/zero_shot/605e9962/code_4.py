from collections import defaultdict

# Step 3: DFS to count white and black vertices in each subtree
def dfs(node, parent):
    # Initialize count as 1 if the node is white, -1 if black
    count = 1 if colors[node] == 'W' else -1
    balanced_subtrees = 0
    
    # Traverse all children
    for child in tree[node]:
        if child != parent:
            # Recursively count for the child subtree
            child_count, child_balanced = dfs(child, node)
            # If the child subtree is balanced, increment the count
            if child_count == 0:
                balanced_subtrees += child_balanced + 1
            # Add the child's count to the current node's count
            count += child_count
    
    return count, balanced_subtrees

# Read number of test cases
t = int(input().strip())

# Handle multiple test cases
for _ in range(t):
    # Step 1: Parse input
    n = int(input().strip())
    parents = list(map(int, input().strip().split()))
    colors = [''] + list(input().strip())  # Adding empty string for 1-indexing

    # Step 2: Tree representation using adjacency lists
    tree = defaultdict(list)
    for i in range(2, n + 1):
        tree[parents[i - 2]].append(i)
        tree[i].append(parents[i - 2])

    # Step 3 and 4: DFS and count balanced subtrees
    _, balanced_subtrees = dfs(1, -1)

    # Step 6: Output the result
    print(balanced_subtrees)
